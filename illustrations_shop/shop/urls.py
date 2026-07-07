from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),    
    path('product/', views.product, name="product"),
    path('illustrations/', views.illustrations, name="illustrations"),
    path('individual_illustrations/', views.individual_illustrations, name="individual_illustrations"),
    path('illustration_packages/', views.illustration_packages, name="illustration_packages"),    
    path('icons/', views.icons, name="icons"),
    path('individual_icons/', views.individual_icons, name="individual_icons"),
    path('icon_sets/', views.icon_sets, name="icon_sets"),
    path('basket/', views.basket, name="basket"),
    path('privacy/', views.privacy, name="privacy"),
    path('conditions/', views.conditions, name="conditions"),
]