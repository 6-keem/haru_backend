from rest_framework import serializers
from .models import Words, Sentence

class SenetnceSerializer(serializers.ModelSerializer):
    class Meta :
        model = Sentence
        field = ['sentence_id', 'kr', 'jp']

class WordsSerializer(serializers.ModelSerializer):
    sentence = SenetnceSerializer()
    
    class Meta:
        model = Words
        fields = ['word_id', 'link', 'word_class', 'star_count',
                  "kanji", "furigana", "word_meaning", "level", "sentence"]