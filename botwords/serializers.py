from rest_framework import serializers
from .models import BotWords




class BotWordsSerializer(serializers.ModelSerializer):

    class Meta:
        model = BotWords
        fields = '__all__'


