from django.urls import path
from .views import WordListView

urlpatterns = [
    path('word/', WordListView.as_view(), name='word'),
]