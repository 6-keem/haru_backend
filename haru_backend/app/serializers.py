from rest_framework import serializers
from .models import Word, Sentence

class SentenceSerializer(serializers.ModelSerializer):
    class Meta :
        model = Sentence
        fields = '__all__'
        # field = ['sentence_id', 'kr', 'jp']

class WordSerializer(serializers.ModelSerializer):
    sentence = SentenceSerializer()
    class Meta:
        model = Word
        fields = '__all__'
        # fields = ['word_id', 'link', 'word_class', 'star_count',
        #           "kanji", "furigana", "word_meaning", "level", "sentence"]