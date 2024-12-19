from django.db import models
from django.contrib.auth.models import User

"""  class Book(models.Model):
    title = models.CharField(max_length=200) 
    author = models.CharField(max_length=100)
    publication_date = models.DateField() 
    isbn = models.CharField(max_length=13, unique=True) 
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    def __str__(self): 
        return self.title
        """

class Supplier(models.Model):
    name = models.CharField(max_length=45, unique=True)  # Поле должно быть уникальным
    city = models.CharField(max_length=20)

class Coffee(models.Model):
    title = models.CharField(max_length=30, unique=True)  # Поле должно быть уникальным
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

class Product_Storage(models.Model):
    title = models.ForeignKey(Coffee, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    count = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    ########ОСТАНОВИЛСЯ НА МЕЙКМИГРЕЙШН#######################
