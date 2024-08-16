from crypt import methods
from os import access
from rest_framework.decorators import action
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Artist, Album, Song, SongsAlbum
from .serializers import AlbumSerializerWeb, ArtistSerializerWeb, SongSerializerWeb, ArtistSerializerTelegram, SongSerializerTelegram, SongsAlbumSerializerWeb, AlbumSerializerTelegram
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework import status


class ArtistViewSetWeb(viewsets.ModelViewSet):
    serializer_class = ArtistSerializerWeb
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    def get_queryset(self):
        return Artist.objects.all()

    @action(detail=True, methods=["GET", ])
    def seen(self, request, *args, **kwargs):
        artist = self.get_object()
        artist.seen += 1
        artist.save()
        return Response(data=artist.listen)

    @action(detail=False, methods=["GET", ])
    def top(self, request, *args, **kwargs):
        artist = self.get_queryset().order_by('-listen')[:3]
        serializer = ArtistSerializerWeb(artist, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class ArtistViewSetTelegram(viewsets.ModelViewSet):
    serializer_class = ArtistSerializerTelegram
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    def get_queryset(self):
        return Artist.objects.all()

    @action(detail=True, methods=["GET", ])
    def seen(self, request, *args, **kwargs):
        artist = self.get_object()
        artist.seen += 1
        artist.save()
        return Response(data=artist.listen)

    @action(detail=False, methods=["GET", ])
    def top(self, request, *args, **kwargs):
        artist = self.get_queryset().order_by('-listen')[:3]
        serializer = ArtistSerializerTelegram(artist, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class AlbumViewSetWeb(viewsets.ModelViewSet):
    serializer_class = AlbumSerializerWeb
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    def get_queryset(self):
        return Album.objects.all()

    @action(detail=True, methods=["GET", ])
    def seen(self, request, *args, **kwargs):
        album = self.get_object()
        album.seen += 1
        album.save()
        return Response(data=album.listen)

    @action(detail=False, methods=["GET", ])
    def top(self, request, *args, **kwargs):
        album = self.get_queryset().order_by('-listen')[:3]
        serializer = AlbumSerializerWeb(album, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class AlbumViewSetTelegram(viewsets.ModelViewSet):
    serializer_class = AlbumSerializerTelegram
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    def get_queryset(self):
        return Album.objects.all()

    @action(detail=True, methods=["GET", ])
    def seen(self, request, *args, **kwargs):
        album = self.get_object()
        album.seen += 1
        album.save()
        return Response(data=album.listen)

    @action(detail=False, methods=["GET", ])
    def top(self, request, *args, **kwargs):
        album = self.get_queryset().order_by('-listen')[:3]
        serializer = AlbumSerializerTelegram(album, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class SongViewSetWeb(viewsets.ModelViewSet):
    serializer_class = SongSerializerWeb
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    def get_queryset(self):
        return Song.objects.all()

    @action(detail=True, methods=["GET", ])
    def listen(self, request, *args, **kwargs):
        song = self.get_object()
        song.listen += 1
        song.save()
        return Response(data=song.listen)

    @action(detail=False, methods=["GET", ])
    def top(self, request, *args, **kwargs):
        songs = self.get_queryset().order_by('-listen')[:3]
        serializer = SongSerializerWeb(songs, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class SongViewSetTelegram(viewsets.ModelViewSet):
    serializer_class = SongSerializerTelegram
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    def get_queryset(self):
        return Song.objects.all()

    @action(detail=True, methods=["GET", ])
    def listen(self, request, *args, **kwargs):
        song = self.get_object()
        song.listen += 1
        song.save()
        return Response(data=song.listen)

    @action(detail=False, methods=["GET", ])
    def top(self, request, *args, **kwargs):
        songs = self.get_queryset().order_by('-listen')[:3]
        serializer = SongSerializerTelegram(songs, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)



class SongsAlbumViewSetWeb(viewsets.ModelViewSet):
    serializer_class = SongsAlbumSerializerWeb
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    def get_queryset(self):
        return SongsAlbum.objects.all()



class TokenCkeck(APIView):
    def get(self, request):
        from rest_framework.authtoken.models import Token

        token = Token.objects.create(username="user1", password="otabek123")
        print(token.key)