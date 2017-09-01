from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255)
    thumbnail = models.FileField()
    body = models.CharField(max_length=5000)
    '''
    organisation
    author
    '''
    def __str__(self):
        return self.title

		
