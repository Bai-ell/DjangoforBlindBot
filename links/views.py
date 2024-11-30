from rest_framework import generics
from .models import Links, Contacts
from .serializers import LinksSerializer, ContactsSerializer

class LinksListCreateAPIView(generics.ListCreateAPIView):
    queryset = Links.objects.all()
    serializer_class = LinksSerializer

class LinksRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Links.objects.all()
    serializer_class = LinksSerializer

class ContactsListCreateAPIView(generics.ListCreateAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer

class ContactsRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer
