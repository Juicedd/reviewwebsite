from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView
from .models import Album, Review, Reviewer, Track, AlbumLink
from .forms import ReviewForm


@login_required
def album_list(request):
    """
    View to display a list of all albums.
    """
    albums = Album.objects.filter(editions__year=2025)
    query = request.GET.get('album_search')

    if query != '' and query is not None:
        albums = albums.filter(
            Q(title__icontains=query) |
            Q(artist__icontains=query)
        ).distinct()

    return render(request, 'album_list.html', {'albums': albums, 'query': query})


@login_required
def album_detail(request, pk):
    """
    View to display details of a specific album.
    """
    album = get_object_or_404(Album, pk=pk)
    tracks = Track.objects.filter(album=album)
    links = AlbumLink.objects.filter(album=album)

    if request.user.is_authenticated:
        try:
            review = Review.objects.get(
                album=album, reviewer__user=request.user)
        except Review.DoesNotExist:
            review = None

    return render(request, 'album_detail.html', {'album': album, 'review': review, 'tracks': tracks, 'links':links})


@login_required
def review_create(request, pk):
    """
    View to displey the album review page.
    """
    album = get_object_or_404(Album, pk=pk)
    reviewer = get_object_or_404(Reviewer, user=request.user)
    tracks = Track.objects.filter(album=album)

    if request.method == 'POST':
        form = ReviewForm(request.POST, album=album)
        if form.is_valid():
            review = form.save(commit=False)
            review.album = album
            review.reviewer = reviewer
            review.save()
            # Redirect to album detail page after successful review submission
            return redirect('album_detail', pk=pk)
    else:
        form = ReviewForm(album=album)

    return render(request, 'review_album.html', {'form': form, 'album': album, 'tracks': tracks})


@login_required
def review_update(request, pk):
    """
    View to displey the album review page.
    """
    review = get_object_or_404(Review, pk=pk)
    tracks = Track.objects.filter(album=review.album)

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review, album=review.album)
        if form.is_valid():
            review.save()
            # Redirect to album detail page after successful review submission
            return redirect('album_detail', pk=review.album_id)
    else:
        form = ReviewForm(instance=review, album=review.album)
    return render(request, 'review_album.html', {'form': form, 'review': review, 'album': review.album, 'tracks': tracks})


@login_required
def pending_reviews(request, user_pk):
    """
    View to display pending reviews for a user.
    """
    reviewer = get_object_or_404(Reviewer,user_id=user_pk)    
    albums = Album.objects.filter(editions__year=2025)
    user_reviews = Review.objects.filter(reviewer=reviewer, album__editions__year=2025)

    # filter for pending albums
    user_review_set = user_reviews.values_list('album_id', flat=True)
    pending_albums = albums.exclude(id__in=user_review_set)

    return render(request, 'pending_reviews.html', {'pending_albums': pending_albums, 'user_reviews':user_reviews})


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
