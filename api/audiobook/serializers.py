from rest_framework import serializers
from audiobook.models import Audiobook



class AudiobookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audiobook
        fields = '__all__'




