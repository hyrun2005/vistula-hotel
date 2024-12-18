from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.menu_page, name='menu_page_rooms'),
    path('<int:room_id>/book/', views.create_booking, name='create_booking'),
    path('<int:room_id>/', views.room_detail, name='room_detail'),
    path('booking/<int:booking_id>/', views.booking_detail, name='booking_detail'),
    path('booking/<int:booking_id>/payment/', views.make_payment, name='make_payment')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
