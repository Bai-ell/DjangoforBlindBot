from rest_framework import serializers
from .models import Links, Contacts

class LinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Links
        fields = '__all__'

class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = '__all__'
