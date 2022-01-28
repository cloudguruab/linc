from django.models import models


class User(models.Model):
    password = models.CharField(max_length=128, unique=True)
    secret = models.CharField(max_length=20, unique=True)
    
    # def __str__(self):
    #     return 