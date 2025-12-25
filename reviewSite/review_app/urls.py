from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.album_list, name='album_list'),
    path('album/<int:pk>/', views.album_detail, name='album_detail'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('album/<int:pk>/create-review', views.review_create, name='review_create'),
    path('album/<int:pk>/update-review', views.review_update, name='review_update'),
    path('my_reviews/', views.my_reviews, name='my_reviews'),
    path('dashboard/',views.placeholder, {'page_name':'Dashboard'}, name='dashboard'),
    path('archive/',views.placeholder, {'page_name':'Archive'}, name='archive'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
