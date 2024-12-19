from rest_framework import serializers 
from .models import Product_Storage, Coffee, Supplier #, Book

""" class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'author', 'title', 'publication_date']

    def validate_title(self, value):
        #Проверка корректности названия произведения.
        if len(value) < 5:
            raise serializers.ValidationError("Title must be more 5 characters long.")
        return value """

class ProductSerializer(serializers.ModelSerializer):
    title = serializers.SlugRelatedField(
        queryset=Coffee.objects.all(),  # Запрос для валидации
        slug_field='title'  # Поле в Coffee, которое будет использоваться вместо id
    )
    supplier = serializers.SlugRelatedField(
        queryset=Supplier.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = Product_Storage
        fields = ['id', 'title', 'supplier', 'count'] 