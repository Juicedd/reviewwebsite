from django.urls import path
from . import views

urlpatterns = [
    path('', views.album_list, name='album_list'),
    path('album/<int:pk>/', views.album_detail, name='album_detail'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('album/<int:pk>/create_review', views.review_create, name='review_create'),
    path('review/<int:pk>/update', views.review_update, name='review_update')
]
