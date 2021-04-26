from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from .models import Songs#,0Podcast,AudioBook
from .serializers import SongsSerializer#,PodcastSerializer,AudioBookSerializer


class SongsApi(generics.ListAPIView):
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer

class SongsCreateApi(generics.ListCreateAPIView):
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer

class SongsUpdateApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer



