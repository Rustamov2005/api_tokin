#Telegram API
#Web Applications
from rest_framework import serializers

from api.models import Artist, Album, Song, SongsAlbum


#Web
class ArtistSerializerWeb(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('id', 'first_name', 'last_name', 'nic_name', 'image', 'seen')


class AlbumSerializerWeb(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('id', 'title', 'artist', 'description', 'seen')


class SongSerializerWeb(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('id', 'title', 'artist', 'description', 'listen')


class SongsAlbumSerializerWeb(serializers.ModelSerializer):
    class Meta:
        model = SongsAlbum
        fields = ('id', 'album', 'songs', 'listen')


#Telegram
class ArtistSerializerTelegram(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('first_name', 'last_name', 'nic_name', 'seen')


class AlbumSerializerTelegram(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('title', 'artist', 'seen', 'status')


class SongSerializerTelegram(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('title', 'artist', 'description', 'listen', 'status')


# class TokenCheck(serializers.Serializer):
#     username = serializers.CharField()
#     password = serializers.CharField()

