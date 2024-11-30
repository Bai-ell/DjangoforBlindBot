# buttons/urls.py
from django.urls import path
from .views import BotWordsListCreate, BotWordsRetrieveUpdateDestroy

urlpatterns = [
    path('botwords/', BotWordsListCreate.as_view(), name='botwords-list-create'),
    path('botwords/<int:pk>/', BotWordsRetrieveUpdateDestroy.as_view(), name='botwords-retrieve-update-destroy'),
]
