from django.urls import path
from .views import QuestionnaireCreateView, QuestionnaireListView, QuestionnaireDetailView, TypeGiftListCreateView, TypeGiftRetrieveUpdateDestroyView

urlpatterns = [
    path('create/', QuestionnaireCreateView.as_view(), name='questionnaire-create'),
    path('list/', QuestionnaireListView.as_view(), name='questionnaire-list'),
    path('detail/<int:id>/', QuestionnaireDetailView.as_view(), name='questionnaire-detail'),
    path('gifts/', TypeGiftListCreateView.as_view(), name='gift-list-create'),
    path('gifts/<int:pk>/', TypeGiftRetrieveUpdateDestroyView.as_view(), name='gift-detail'),
]
