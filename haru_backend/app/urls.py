from django.urls import path
from .views import WordListView, TestWordListView

urlpatterns = [
    path('word/', WordListView.as_view(), name='word'),
    path('word-test/', TestWordListView.as_view(), name='word'),
]