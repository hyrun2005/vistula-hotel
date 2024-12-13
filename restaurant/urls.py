from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.mainPageRes, name='restaurantHomePage'),
    path('menu/', views.menu_view, name='menu'),
    path('basket/', views.basket_view, name='basket'),
    path('basket/add/<int:dish_id>/', views.add_to_basket, name='add_to_basket'),
    path('basket/delete/<int:dish_id>/', views.delete_from_basket, name='delete_from_basket'),
    path('order/', views.order_view, name='order'),
]


# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

