from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

class Article(models.Model):
    title = models.CharField(max_length=255)
    thumbnail = models.FileField()
    body = models.CharField(max_length=5000)
    owner = models.ForeignKey('auth.User', related_name='activities', on_delete=models.CASCADE)
    '''
    organisation
    author
    '''
    def __str__(self):
        return self.title

        

		
