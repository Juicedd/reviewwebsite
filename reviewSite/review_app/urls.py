from django.urls import path
from . import views

urlpatterns = [
    path('', views.album_list, name='album_list'),
    path('album/<int:pk>/', views.album_detail, name='album_detail'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
]
