from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Word
from .serializers import WordSerializer
from drf_spectacular.utils import *
from django.db.models import QuerySet
import random


def split_words_by_chapter(words, chapter):
    """
    단어 목록을 chapter에 따라 나누어 반환하는 함수
    """
    total_words = len(words)
    words_per_chapter = total_words // 8
    start_index = (chapter - 1) * words_per_chapter
    end_index = start_index + words_per_chapter

    # 마지막 chapter인 경우에는 남은 모든 단어를 반환
    if chapter == 8:
        return words[start_index:]
    
    return words[start_index:end_index]

def validate_level_and_chapter(level, chapter):
    """
    level과 chapter 값의 유효성을 검사하는 함수
    """
    if level is None:
        raise ValueError("Level parameter is required.")
    
    level = int(level)
    if level <= 0 or level > 5:
        raise ValueError("Level out of range.")
    
    if chapter is not None:
        chapter = int(chapter)
        if chapter <= 0 or chapter > 8:
            raise ValueError("Chapter out of range.")
    
    return level, chapter

class WordListView(APIView):
    @extend_schema(
        summary="단어 조회",
        description="Retrieve JLPT words",
        responses={
            status.HTTP_200_OK: WordSerializer(),
        },
        parameters=[
            OpenApiParameter(
                name='level',
                type=int,
                location=OpenApiParameter.QUERY,
                required=True,
                description='The JLPT level for filtering words'
            ),
            OpenApiParameter(
                name='chapter',
                type=int,
                location=OpenApiParameter.QUERY,
                required=False,
                description='The chapter for filtering words',
            ),
        ],
        tags=["단어"]
    )
    
    def get(self, request):
        try:
            level = request.GET.get('level')
            chapter = request.GET.get('chapter')

            # Level과 Chapter 유효성 검사
            level, chapter = validate_level_and_chapter(level, chapter)

            words = Word.objects.filter(level=level)
            
            # chapter 값이 제공되면, 단어를 chapter별로 분할하여 반환
            if chapter is not None:
                words = split_words_by_chapter(words, chapter)

            serializer = WordSerializer(words, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            print(f"Error: {str(e)}")
            return Response({"error": "BAD REQUEST"}, status=status.HTTP_400_BAD_REQUEST)

class TestWordListView(APIView):
    @extend_schema(
        summary="시험 단어 조회",
        responses={
            status.HTTP_200_OK: WordSerializer(),
        },
        parameters=[
            OpenApiParameter(
                name='level',
                type=int,
                location=OpenApiParameter.QUERY,
                required=True,
                description='The JLPT level for filtering words'
            )
        ],
        tags=["단어"]
    )
    def get(self, requset):
        try :
            level = requset.GET.get('level')
            level, chapter = validate_level_and_chapter(level, None)

            words = Word.objects.filter(level = level)
            if isinstance(words, QuerySet) :
                words = list(words)
            sample_words = random.sample(words, min(len(words), 50))
            serializer = WordSerializer(sample_words, many = True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            print(f"Error: {str(e)}")
            return Response({"error": "BAD REQUEST"}, status=status.HTTP_400_BAD_REQUEST)
