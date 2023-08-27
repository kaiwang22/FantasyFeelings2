from rest_framework import serializers
from .models import NFLPlayer, SentimentEntry

class SentimentEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = SentimentEntry
        fields = '__all__'

class NFLPlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = NFLPlayer
        fields = ['id', 'name', 'position', 'team', 'current_feeling']
