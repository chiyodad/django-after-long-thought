from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200, verbose_name="질문")
    pub_date = models.DateTimeField('date published')

    def __str__(self): # python2 __unicode__
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200, verbose_name="선택지")
    votes = models.IntegerField(default=0, verbose_name="득표수")

    def __str__(self):
        return self.choice_text
