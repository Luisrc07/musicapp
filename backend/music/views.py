from django.shortcuts import render
from rest_framework import viewsets
from .models import Artist, Album, Song
from .serializers import ArtistSerializer, AlbumSerializer, SongSerializer

class ArtistViewSet(viewsets.ModelViewSet):
    """
    Lógica para manejar Artistas
    """
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class AlbumViewSet(viewsets.ModelViewSet):
    """
    Lógica para manejar Álbumes
    """
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class SongViewSet(viewsets.ModelViewSet):
    """
    Lógica para manejar Canciones
    """
    queryset = Song.objects.all()
    serializer_class = SongSerializer

