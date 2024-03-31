from django.contrib import admin
from .models import Album, Review

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist')

# Register the Album model with the custom album listing
admin.site.register(Album, AlbumAdmin)
admin.site.register(Review)