from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name="home"),
    path('shipping_policy/', views.shipping, name="shipping"),
    path('about_us/', views.about_us(request), name="about_us"),
]
