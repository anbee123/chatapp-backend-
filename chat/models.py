from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=10)
    email = models.EmailField()
    password = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_name
