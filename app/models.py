from django.db import models
from django.contrib.auth.models import User

# Определение класса MyModel, который наследует модель Django Model
class MyModel(models.Model):
    # Определение поля id типа AutoField как первичного ключа
    id = models.AutoField(primary_key=True)
    # Определение поля phone типа CharField с максимальной длиной в 20 символов
    phone = models.CharField(max_length=20)

    # Определение метода __str__, который будет использоваться для представления экземпляров модели в виде строки
    def __str__(self):
        return self.phone


class Book(models.Model):
    title = models.CharField(max_length=200) 
    author = models.CharField(max_length=100)
    publication_date = models.DateField() 
    isbn = models.CharField(max_length=13, unique=True) 
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    def __str__(self): 
        return self.title

