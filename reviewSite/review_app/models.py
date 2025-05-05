from django.db import models # type: ignore
from django.contrib.auth.models import User # type: ignore
from django.core.validators import MinValueValidator, MaxValueValidator # type: ignore


class Album(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    release_date = models.DateField()
    cover_image = models.ImageField(upload_to="cover_art/", null=True, blank=True)

    def __str__(self):
        return f"{self.artist} - {self.title} - Album {self.id}"


class Track(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    track_number = models.IntegerField(validators=[MinValueValidator(1)])
    def __str__(self):
        return f"{self.title}"


class Reviewer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(
        upload_to="profile_pictures/", null=True, blank=True
    )

    def __str__(self):
        return f'{self.user.username} Profile'


class Review(models.Model):
    reviewer = models.ForeignKey(
        Reviewer, 
        on_delete=models.CASCADE, 
        related_name="reviews", 
        null=True, 
        blank=True
    )
    album = models.ForeignKey(
        Album, 
        on_delete=models.CASCADE, 
        related_name="reviews"
    )
    content = models.TextField()
    album_score = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        default=0
    )
    cover_score = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        default=0
    )

    favorite_track = models.ForeignKey(
        Track,
        on_delete=models.SET_NULL,
        related_name='review_favtrack',
        null=True,
        blank=True
    )
    worst_track = models.ForeignKey(
        Track,
        on_delete=models.SET_NULL,
        related_name='review_worsttrack',
        null=True,
        blank=True
    )

    def __str__(self):
        return f"Review by {self.reviewer.name} for Album {self.album.id}"

    class Meta:
        unique_together = ["reviewer", "album"]


class Edition(models.Model):
    year = models.IntegerField()
    album = models.ForeignKey(
        Album, 
        on_delete=models.CASCADE, 
        related_name="editions"
    )

    class Meta: 
        unique_together = ["year", "album"]
        ordering = ["-year", 'album']

    def __str__(self):
        return f"Edition {self.year}, where albums are reviewed from {self.year - 1}"

class AlbumLink(models.Model):
    LINK_TYPES = (
        ('youtube', 'YouTube'),
        ('spotify', 'Spotify'),
        ('tidal', 'Tidal'),
        ('apple_music', 'Apple Music')
    )

    album = models.ForeignKey('Album', on_delete=models.CASCADE, related_name='links')
    url = models.URLField()
    link_type = models.CharField(max_length=20, choices=LINK_TYPES)

    class Meta:
        unique_together = ['album', 'link_type', 'url']  # Prevent exact duplicates