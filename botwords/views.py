
from rest_framework import generics
from .models import BotWords
from .serializers import BotWordsSerializer

class BotWordsListCreate(generics.ListCreateAPIView):
    queryset = BotWords.objects.all()
    serializer_class = BotWordsSerializer

class BotWordsRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BotWords.objects.all()
    serializer_class = BotWordsSerializer
