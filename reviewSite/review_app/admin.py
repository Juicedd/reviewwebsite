from django.contrib import admin # type: ignore
from .models import Album, Review, Reviewer, Edition

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist')

class EditionAdmin(admin.ModelAdmin):
    list_display = ('year', 'album')
    list_filter = ('year',)
    search_fields = ('album__title')
    
# Register the Album model with the custom album listing
admin.site.register(Album, AlbumAdmin)
admin.site.register(Review)
admin.site.register(Reviewer)
admin.site.register(Edition)