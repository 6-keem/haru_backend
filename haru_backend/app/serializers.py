from rest_framework import serializers
from drf_spectacular.utils import OpenApiExample
from .models import Word

class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = '__all__'
