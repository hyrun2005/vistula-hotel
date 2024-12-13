from django.contrib import admin
from .models import UserProfile, Room, Booking, Payment

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'phone_number', 'email', 'address')

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_type', 'number', 'price_per_night', 'is_available')
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'room', 'check_in', 'check_out', 'booking_date', 'total_price')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('booking', 'amount', 'payment_date', 'status')
