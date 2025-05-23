from django.urls import path
from . import views

urlpatterns = [
    path('', views.album_list, name='album_list'),
    path('album/<int:pk>/', views.album_detail, name='album_detail'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('album/<int:pk>/create-review', views.review_create, name='review_create'),
    path('review/<int:pk>/update-review', views.review_update, name='review_update'),
    path('user/<int:user_pk>/pending_reviews', views.pending_reviews, name='pending_reviews')
]
