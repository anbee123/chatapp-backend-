from django.db import models

# Create your models here.
class Message(models.Model):
    sender = models.ChartField(max_length=50)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
