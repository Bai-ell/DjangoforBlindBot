from rest_framework import serializers
from .models import Buttons




class ButtonsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Buttons
        fields = '__all__'

