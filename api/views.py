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

    @action(detail=True, methods=["GET", ])
    def listen(self, request, *args, **kwargs):
        song = self.get_object()
        song.listen += 1
        song.save()
        return Response(data=song.listen)


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