import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    def __str__(self):
        return self.txtQuestion
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days = 1)
    
    txtQuestion = models.CharField(max_length=200)
    pub_date = models.DateTimeField('data de publicacao')
    
class Choice(models.Model):
    def __str__(self):
        return self.txtChoice
    
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    txtChoice = models.CharField(max_length = 200)
    votes = models.IntegerField(default=0)
