from django.db import models
from .helpers import SaveMediaFiles


class Artist(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    image = models.URLField()
    nic_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ['id']


class Album(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to=SaveMediaFiles.save_album_image)
    description = models.TextField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Song(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to=SaveMediaFiles.save_song_image)
    description = models.TextField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)


class SongsAlbum(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    songs = models.ManyToManyField(Song)
