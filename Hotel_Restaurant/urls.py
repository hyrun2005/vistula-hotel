from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('acc/', include('accounts.urls')),
    path('payment/', include('payments.urls')),
    path('restaurant/', include('restaurant.urls')),
    path('rooms/', include('hotel_rooms.urls'))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
