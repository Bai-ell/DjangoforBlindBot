from rest_framework import serializers
from .models import Questionnaire, TypeGift

class QuestionnaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questionnaire
        fields = '__all__' 


class TypeGiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeGift
        fields = '__all__'