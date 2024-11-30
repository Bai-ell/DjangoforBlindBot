from rest_framework import serializers
from .models import Institution, Mta




class InstitutionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Institution
        fields = '__all__'

class MtaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mta
        fields = '__all__'


