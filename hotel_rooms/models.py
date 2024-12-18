from django.contrib.auth.models import User
from django.utils import timezone

from django.db import models

# Room Model
class Room(models.Model):
    ROOM_TYPES = [
        ('SINGLE', 'Single'),
        ('DOUBLE', 'Double'),
        ('MORE', 'More'),
    ]

    room_type = models.CharField(max_length=10, choices=ROOM_TYPES)
    number = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.room_type} - Room {self.number}"


# RoomPhoto Model for storing multiple photos per Room
class RoomPhoto(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='photos')
    photo = models.ImageField(upload_to='rooms/photos/')

    def __str__(self):
        return f"Photo for {self.room.room_type} - Room {self.room.number}"

# Booking model to manage user bookings
class Booking(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('CONFIRMED', 'Confirmed'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    booking_date = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')

    def __str__(self):
        return f"Booking {self.id} - {self.status}"


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