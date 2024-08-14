#Telegram API
#Web Applications
from rest_framework import serializers

from api.models import Artist, Album, Song, SongsAlbum


#Web
class ArtistSerializerWeb(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('id', 'first_name', 'last_name', 'nic_name', 'image')


class AlbumSerializerWeb(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('id', 'title', 'artist', 'description')


class SongSerializerWeb(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('id', 'title', 'artist', 'description')


class SongsAlbumSerializerWeb(serializers.ModelSerializer):
    class Meta:
        model = SongsAlbum
        fields = ('id', 'album', 'songs')


#Telegram
class ArtistSerializerTelegram(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('first_name', 'last_name', 'nic_name')


class AlbumSerializerTelegram(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('title', 'artist')


class SongSerializerTelegram(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('title', 'artist', 'description')

