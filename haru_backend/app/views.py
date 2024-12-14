from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Word, Sentence
from .serializers import WordSerializer, SentenceSerializer
from drf_spectacular.utils import *

class WordListView(APIView):
    @extend_schema(
        summary="단어 조회",
        description="Retrieve JLPT words",
        responses={
            status.HTTP_200_OK : WordSerializer(),
        }
    )
    def get(self, request) :
        words = Word.objects.all()
        serializer = WordSerializer(words, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class SentenceListView(APIView):
    @extend_schema(
        summary="문장 조회",
        description="Retrieve sentences associated with JLPT words",
        responses={
            status.HTTP_200_OK: SentenceSerializer(many=True),
        }
    )
    def get(self, request):
        sentences = Sentence.objects.all()
        serializer = SentenceSerializer(sentences, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)