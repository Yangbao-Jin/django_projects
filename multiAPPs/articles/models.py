'''from django.db import models

# Create your models here.'''
from django.db import models
from users.models import CustomUser


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
