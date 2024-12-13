from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Room model to represent hotel rooms
class Room(models.Model):
    ROOM_TYPES = [
        ('SINGLE', 'Single'),
        ('DOUBLE', 'Double'),
        ('SUITE', 'Suite'),
    ]

    room_type = models.CharField(max_length=10, choices=ROOM_TYPES)
    number = models.CharField(max_length=10, unique=True)
    description = models.TextField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.room_type} - Room {self.number}"


# Booking model to manage user bookings
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    booking_date = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Booking {self.id} by {self.user.username}"

    def calculate_total_price(self):
        days = (self.check_out - self.check_in).days
        return days * self.room.price_per_night


# Payment model to track payments for bookings
class Payment(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=[('PAID', 'Paid'), ('PENDING', 'Pending')])

    def __str__(self):
        return f"Payment for Booking {self.booking.id} - {self.status}"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15, blank=True, default="")
    email = models.EmailField()
    address = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.firstname
