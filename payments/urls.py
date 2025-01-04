from django.urls import path
from . import views

urlpatterns = [
    path('confirm_order/', views.confirm_order, name='confirm_order'),
    path('payment_success/', views.payment_successful, name='payment_success'),
    path('payment_failed/', views.payment_failed, name='payment_failed'),
    path('payment_callback/', views.payment_callback, name='payment_callback'),
]
