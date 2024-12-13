from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.mainPage, name='homePage'),
    path('contactUs/', views.contactPage, name='contactUs'),
    path('about/', views.aboutPage, name='aboutUs'),
]
