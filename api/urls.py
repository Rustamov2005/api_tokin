from django.urls import path, include
from rest_framework import routers
from .views import ArtistViewSetWeb, ArtistViewSetTelegram, AlbumViewSetTelegram, ArtistSerializerWeb, \
    SongSerializerWeb, SongSerializerTelegram, SongsAlbumSerializerWeb, AlbumViewSetWeb, SongViewSetWeb, \
    SongViewSetTelegram
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'artists-w', ArtistViewSetWeb, basename='artists-w')
router.register(r'artist-t', ArtistViewSetTelegram, basename='artist-t')
router.register(r'albums-w', AlbumViewSetWeb, basename='albums-w')
router.register(r'album-t', AlbumViewSetTelegram, basename='album-t')
router.register(r'songs-w', SongViewSetWeb, basename='songs-w')
router.register(r'songs-t', SongViewSetTelegram, basename='songs-t')
router.register(r'songs-album-w', SongViewSetWeb, basename='songs-album-w')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', obtain_auth_token),
]
