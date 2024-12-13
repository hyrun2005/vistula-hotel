from . import views
from django.urls import path

urlpatterns = [
    path('', views.login_in, name='login_in'),
    path('register/', views.registration, name='reg_user'),
    path('logout_user/', views.logoutUser, name='logout_user')
]
