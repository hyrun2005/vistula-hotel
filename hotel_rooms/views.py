from django.shortcuts import render
from .models import Room

def menu_page(request):
    rooms = Room.objects.prefetch_related('photos').all()  # Fetch rooms with photos
    return render(request, 'menu_rooms.html', {'rooms': rooms})
