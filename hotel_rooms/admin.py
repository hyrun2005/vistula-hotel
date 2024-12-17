from django.contrib import admin
from .models import Room, Booking, Payment, RoomPhoto

class RoomPhotoInline(admin.TabularInline):
    model = RoomPhoto
    extra = 1


# Room Admin with Photo Inline
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_type', 'number', 'price_per_night', 'is_available')
    inlines = [RoomPhotoInline]  # Attach the inline for RoomPhoto

# Booking Admin
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'room', 'check_in', 'check_out', 'booking_date', 'total_price')

# Payment Admin
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('booking', 'amount', 'payment_date', 'status')

# Optional: Register RoomPhoto independently (if needed)
@admin.register(RoomPhoto)
class RoomPhotoAdmin(admin.ModelAdmin):
    list_display = ('room', 'photo')
