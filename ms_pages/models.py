from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    """ A topic about maplestory """
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User)
    
    def __str__(self):
        """ represent topic with a string of it's name """
        return self.text

class Entry(models.Model):
    """ Things relate to a topic """
    topic = models.ForeignKey(Topic)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add= True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """ represent entry with first 50 characters """
        return self.text[:50] + '...'
