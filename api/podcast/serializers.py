from rest_framework import serializers
from podcast.models import Podcast



class PodcastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Podcast
        fields = '__all__'






