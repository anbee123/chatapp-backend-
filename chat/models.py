from django.db import models
from datetime import datetime

# Create your models here.
class Chat(models.Model):
    userName = models.CharField(max_length=255)
    roomName = models.CharField(max_length=255)
    message = models.TextField(blank=True)

def __str__(self):
    return self.name

