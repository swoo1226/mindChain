from django.db import models


class Words(models.Model):
    id = models.IntegerField(primary_key=True)
    content = models.TextField()
    word_type = models.TextField()
    word_length = models.IntegerField(default=0)
    first_sound = models.TextField()
    last_sound = models.TextField()
    simple = models.BooleanField(default=False)
    pos = models.TextField()
    noun = models.BooleanField(default=False)
    very_simple = models.BooleanField(default=False)
    consonants = models.TextField()
