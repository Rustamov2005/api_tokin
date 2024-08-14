from django.contrib import admin
from .models import Artist, Album, SongsAlbum, Song

admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(SongsAlbum)
admin.site.register(Song)
