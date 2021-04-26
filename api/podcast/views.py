from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from .models import Podcast
from .serializers import PodcastSerializer


class PodcastApi(generics.ListAPIView):
    queryset = Podcast.objects.all()
    serializer_class = PodcastSerializer

class PodcastCreateApi(generics.ListCreateAPIView):
    queryset = Podcast.objects.all()
    serializer_class = PodcastSerializer

class PodcastUpdateApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Podcast.objects.all()
    serializer_class = PodcastSerializer
