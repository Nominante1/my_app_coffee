from django.shortcuts import render
from rest_framework import viewsets 
from .models import Book 
from .serializers import BookSerializer 
from rest_framework.permissions import IsAuthenticated

class BookViewSet(viewsets.ModelViewSet): 
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user) # cохраняем объект, связывая его с пользователем, который инициировал запрос

# Create your views here.
