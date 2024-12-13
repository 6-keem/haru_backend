from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Word, Sentence
from .serializers import WordSerializer, SenetnceSerializer

class WordListView(APIView):
    def get(self, request) :
        words = Word.objects.all()
        serializer = WordSerializer(words, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class SentenceListView(APIView):
    def get(self, request):
        sentences = Sentence.objects.all()
        serializer = SenetnceSerializer(sentences, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)