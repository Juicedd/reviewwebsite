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
    title = models.CharField(max_length=50)
    track_number = models.IntegerField(MinValueValidator(1))
    def __str__(self):
        return f"{self.title} by {self.album.artist}"


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
    reviewer = models.ForeignKey(Reviewer, on_delete=models.CASCADE, related_name="reviews", null=True, blank=True )
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="reviews")
    content = models.TextField()
    album_score = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)], default=0
    )
    cover_score = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)], default=0
    )
    favorite_track = models.CharField(max_length=255, null=True, blank=True)
    worst_track = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"Review by {self.reviewer.name} for Album {self.album.id}"

    class Meta:
        unique_together = ["reviewer", "album"]
