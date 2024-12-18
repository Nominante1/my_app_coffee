from django.shortcuts import render
from rest_framework import viewsets 
from .models import Product_Storage #, Book
from .serializers import ProductSerializer #, BookSerializer, 
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.decorators import api_view

@swagger_auto_schema(method='post', responses={200: 'Success'})#создание декоратора для создания схемы swagger
@api_view(['POST'])
def some_protected_view(request):
    return Response({"message": "This is a protected view!"})

""" class BookViewSet(viewsets.ModelViewSet): 
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  """

# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product_Storage.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated] #доступ только для авторизованных пользователей

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)