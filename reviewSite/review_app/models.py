from django.db import models
from django.contrib.auth.models import User


def get_upload_path(instance, filename):
    # Assuming Album model has a ForeignKey to Artist model
    # You can adjust this function based on your actual model structure
    album_title = instance.title.replace(" ", "_").lower()
    return f"cover_art/{album_title}/{filename}"

class Album(models.Model):
    title = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    release_date = models.DateField()
    cover_image = models.ImageField(upload_to=get_upload_path, null=True, blank=True)

    def __str__(self):
        return self.title

class Review(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100)
    comment = models.TextField()
    rating_music = models.IntegerField()
    rating_cover = models.IntegerField()

    def __str__(self):
        return f"{self.user_name} - {self.album.title}"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    def __str__(self):
        return self.user.username