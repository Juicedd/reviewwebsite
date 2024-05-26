from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Album, Review

def album_list(request):
    """
    View to display a list of all albums.
    """
    albums = Album.objects.all()
    return render(request, 'album_list.html', {'albums': albums})

def album_detail(request, pk):
    """
    View to display details of a specific album.
    """
    album = get_object_or_404(Album, pk=pk)
    return render(request, 'album_detail.html', {'album': album})

def about(request):
    """
    View to display the about page.
    """
    return render(request, 'about.html')

def contact(request):
    """
    View to display the contact page.
    """
    return render(request, 'contact.html')