from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.views.generic import ListView, DetailView
from .models import Album, Review
from .forms import AlbumReviewForm

def album_list(request):
    """
    View to display a list of all albums.
    """
    albums = Album.objects.all()
    query = request.GET.get('album_search')

    if query != '' and query is not None:
        albums = albums.filter(
            Q(title__icontains=query) |
            Q(artist__icontains=query)
            ).distinct()
        
    return render(request, 'album_list.html', {'albums': albums, 'query':query})

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

def review_album(request):
    """
    View to displey the album review page.
    """
    if request.method == 'POST':
        form = AlbumReviewForm(request.POST)
        if form.is_valid():
            # Do something with the form data
            pass
    else:
        form = ContactForm()

    return render(request, 'review_album.html')