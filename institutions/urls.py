from django.urls import path
from .views import (
    InstitutionsListCreate,
    InstitutionsRetrieveUpdateDestroy,
    MTACreate,
    MTARetrieveUpdateDestroy,
)

urlpatterns = [
    path('institutions/', InstitutionsListCreate.as_view(), name='med-list-create'),
    path('institution/<int:pk>/', InstitutionsRetrieveUpdateDestroy.as_view(), name='med-detail'),
    path('mta/', MTACreate.as_view(), name='mta-list-create'),
    path('mta/<int:pk>/', MTARetrieveUpdateDestroy.as_view(), name='mta-detail'),
]
