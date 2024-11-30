# buttons/urls.py
from django.urls import path
from .views import ButtonsListCreate, ButtonsRetrieveUpdateDestroy

urlpatterns = [
    path('buttons/', ButtonsListCreate.as_view(), name='buttons-list-create'),
    path('buttons/<int:pk>/', ButtonsRetrieveUpdateDestroy.as_view(), name='buttons-retrieve-update-destroy'),
]
