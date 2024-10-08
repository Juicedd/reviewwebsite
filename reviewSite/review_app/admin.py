from django.contrib import admin # type: ignore
from .models import Album, Review, Reviewer

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist')

# Register the Album model with the custom album listing
admin.site.register(Album, AlbumAdmin)
admin.site.register(Review)
admin.site.register(Reviewer)