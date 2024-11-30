# buttons/views.py
from rest_framework import generics
from .models import Buttons
from .serializers import ButtonsSerializer

class ButtonsListCreate(generics.ListCreateAPIView):
    queryset = Buttons.objects.all()
    serializer_class = ButtonsSerializer

class ButtonsRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Buttons.objects.all()
    serializer_class = ButtonsSerializer
