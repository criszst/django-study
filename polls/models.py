import datetime

from django.contrib import admin
from django.db import models
from django.utils import timezone

class Question(models.Model):
    def __str__(self):
        return self.txtQuestion
    
    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Publicado recentemente?',
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    
    txtQuestion = models.CharField(max_length=200)
    pub_date = models.DateTimeField('data de publicacao')
    
class Choice(models.Model):
    def __str__(self):
        return self.txtChoice
    
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    txtChoice = models.CharField(max_length = 200)
    votes = models.IntegerField(default=0)
