from rest_framework import serializers
from audio.models import Songs #,Podcast,AudioBook

class SongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = '__all__'


'''       


class AudioBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioBook
        fields = '__all__'

'''









