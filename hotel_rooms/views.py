from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Room, RoomPhoto, Booking, Payment
from django.contrib.auth.decorators import login_required
from django.utils.timezone import make_aware
from datetime import datetime
from accounts.views import custom_login_required


def menu_page(request):
    rooms = Room.objects.prefetch_related('photos').all()  # Fetch rooms with photos
    return render(request, 'menu_rooms.html', {'rooms': rooms})


def room_detail(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    room.refresh_from_db()  # Ensure the latest data is fetched
    return render(request, 'room_detail.html', {'room': room})


@custom_login_required
def create_booking(request, room_id):
    room = get_object_or_404(Room, id=room_id)

    if request.method == 'POST':
        check_in = request.POST.get('check_in')
        check_out = request.POST.get('check_out')

        if not check_in or not check_out:
            messages.error(request, "Both check-in and check-out dates are required.")
            return render(request, 'create_booking.html', {'room': room})

        try:
            check_in_date = make_aware(datetime.strptime(check_in, '%Y-%m-%d'))
            check_out_date = make_aware(datetime.strptime(check_out, '%Y-%m-%d'))
        except ValueError:
            messages.error(request, "Invalid date format. Use YYYY-MM-DD.")
            return render(request, 'create_booking.html', {'room': room})

        if check_in_date >= check_out_date:
            messages.error(request, "Check-out date must be after check-in date.")
            return render(request, 'create_booking.html', {'room': room})

        # Check for overlapping bookings
        overlapping_bookings = Booking.objects.filter(
            room=room,
            check_in__lt=check_out_date,
            check_out__gt=check_in_date,
            status='CONFIRMED'  # Only consider confirmed bookings for overlaps
        )

        if overlapping_bookings.exists():
            messages.error(request, "This room is already booked for the selected dates.")
            return render(request, 'create_booking.html', {'room': room, 'check_in': check_in, 'check_out': check_out})

        # Create the booking in a pending state
        booking = Booking.objects.create(
            user=request.user,
            room=room,
            check_in=check_in_date,
            check_out=check_out_date,
            total_price=(check_out_date - check_in_date).days * room.price_per_night,
            status='PENDING'  # New status for pending bookings
        )

        messages.success(request, "Booking initiated! Complete the payment to confirm.")
        return redirect('booking_detail', booking_id=booking.id)

    return render(request, 'create_booking.html', {'room': room})

@custom_login_required
def booking_detail(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    user_email = request.user.email
    return render(request, 'booking_detail.html', {
        'booking': booking,
        'user_email': user_email
    })

@custom_login_required
def make_payment(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    if request.method == 'POST':
        Payment.objects.create(
            booking=booking,
            amount=booking.total_price,
            status='PAID'
        )

        # Mark booking as confirmed and the room as unavailable
        booking.status = 'CONFIRMED'
        booking.save()
        booking.room.is_available = False
        booking.room.save()

        # Send payment confirmation email
        subject = "Payment Confirmation"
        message = (
            f"Dear {request.user.first_name},\n\n"
            f"Your payment has been successfully processed. Here are your booking details:\n"
            f"Room: {booking.room.room_type} - Room {booking.room.number}\n"
            f"Check-in Date: {booking.check_in}\n"
            f"Check-out Date: {booking.check_out}\n"
            f"Total Amount Paid: ${booking.total_price}\n\n"
            f"Thank you for choosing our services! We look forward to seeing you soon."
        )
        recipient_list = [request.user.email]
        send_mail(subject, message, 'noreply@hotel.com', recipient_list, fail_silently=False)

        messages.success(request, "Payment successful! Booking confirmed.")
        return redirect('booking_detail', booking_id=booking.id)

    return render(request, 'make_payment.html', {'booking': booking})

