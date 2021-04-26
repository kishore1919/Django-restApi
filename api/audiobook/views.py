from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from .models import Audiobook
from .serializers import AudiobookSerializer


class AudiobookApi(generics.ListAPIView):
    queryset = Audiobook.objects.all()
    serializer_class = AudiobookSerializer

class AudiobookCreateApi(generics.ListCreateAPIView):
    queryset = Audiobook.objects.all()
    serializer_class = AudiobookSerializer

class AudiobookUpdateApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Audiobook.objects.all()
    serializer_class = AudiobookSerializer
