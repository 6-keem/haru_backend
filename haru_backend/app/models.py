from django.db import models

class Sentence(models.Model):
    sentence_id = models.AutoField(primary_key=True)
    kr = models.TextField()
    jp = models.TextField()
    
    def __str__(self):
        return f"{self.kr, self.jp}"

class Words(models.Model):
    word_id = models.IntegerField(primary_key=True, max_length=11)
    link = models.TextField(max_length=50)
    word_class = models.CharField(max_length=50)
    star_count = models.IntegerField(max_length=11)
    kanji = models.CharField(max_length=50)
    furigana = models.CharField(max_length=50)
    word_meaning = models.TextField()
    level = models.IntegerField(max_length=11)
    sentence = models.ForeignKey(Sentence, on_delete=models.CASCADE)

    def __self__(self):
        return self