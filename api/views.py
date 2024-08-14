from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Artist, Album, Song, SongsAlbum
from .serializers import AlbumSerializerWeb, ArtistSerializerWeb, SongSerializerWeb, ArtistSerializerTelegram, SongSerializerTelegram, SongsAlbumSerializerWeb, AlbumSerializerTelegram
from rest_framework.authentication import TokenAuthentication


class ArtistViewSetWeb(viewsets.ModelViewSet):
    serializer_class = ArtistSerializerWeb
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    def get_queryset(self):
        return Artist.objects.all()


class ArtistViewSetTelegram(viewsets.ModelViewSet):
    serializer_class = ArtistSerializerTelegram
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    def get_queryset(self):
        return Artist.objects.all()


class AlbumViewSetWeb(viewsets.ModelViewSet):
    serializer_class = AlbumSerializerWeb
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    def get_queryset(self):
        return Album.objects.all()


class AlbumViewSetTelegram(viewsets.ModelViewSet):
    serializer_class = AlbumSerializerTelegram
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    def get_queryset(self):
        return Album.objects.all()


class SongViewSetWeb(viewsets.ModelViewSet):
    serializer_class = SongSerializerWeb
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    def get_queryset(self):
        return Song.objects.all()


class SongViewSetTelegram(viewsets.ModelViewSet):
    serializer_class = SongSerializerTelegram
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    def get_queryset(self):
        return Song.objects.all()


class SongsAlbumViewSetWeb(viewsets.ModelViewSet):
    serializer_class = SongsAlbumSerializerWeb
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    def get_queryset(self):
        return SongsAlbum.objects.all()
