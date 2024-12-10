from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=200) 
    author = models.CharField(max_length=100)
    publication_date = models.DateField() 
    isbn = models.CharField(max_length=13, unique=True) 
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    def __str__(self): 
        return self.title

