from django.db import models

class Word(models.Model):
    word_id = models.IntegerField(primary_key=True)
    link = models.TextField(max_length=50)
    word_class = models.CharField(max_length=50)
    star_count = models.IntegerField()
    kanji = models.CharField(max_length=50)
    furigana = models.CharField(max_length=50)
    word_meaning = models.TextField()
    level = models.IntegerField()
    sentences = models.TextField()

    class Meta:
        db_table = 'word'

    def __self__(self):
        return self