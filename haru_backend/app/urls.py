from django.urls import path
from .views import WordListView, SentenceListView

urlpatterns = [
    path('words/', WordListView.as_view(), name='word-list'),
    path('sentences/', SentenceListView.as_view(), name='sentence-list')
]