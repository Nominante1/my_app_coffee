from rest_framework import serializers 
from .models import Book 

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'author', 'title', 'publication_date']

    def validate_title(self, value):
        """
        Проверка корректности названия произведения.
        """
        if len(value) < 5:
            raise serializers.ValidationError("Title must be more 5 characters long.")
        return value
