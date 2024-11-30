from rest_framework import generics
from .models import Questionnaire, TypeGift
from .serializers import QuestionnaireSerializer, TypeGiftSerializer


class QuestionnaireCreateView(generics.CreateAPIView):
    queryset = Questionnaire.objects.all()
    serializer_class = QuestionnaireSerializer


class QuestionnaireListView(generics.ListAPIView):
    queryset = Questionnaire.objects.all()
    serializer_class = QuestionnaireSerializer

class QuestionnaireDetailView(generics.RetrieveUpdateAPIView):
    queryset = Questionnaire.objects.all()
    serializer_class = QuestionnaireSerializer
    lookup_field = 'id'



class TypeGiftListCreateView(generics.ListCreateAPIView):
    queryset = TypeGift.objects.all()
    serializer_class = TypeGiftSerializer

class TypeGiftRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TypeGift.objects.all()
    serializer_class = TypeGiftSerializer