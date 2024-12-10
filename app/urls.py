from django.urls import path, include 
from rest_framework.routers import DefaultRouter
from .views import BookViewSet 
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import BookViewSet  # Ваши представления


router = DefaultRouter() 
router.register(r'books', BookViewSet) 
urlpatterns = [ 
        path('api/', include(router.urls)), 
        path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Получение токена
        path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Обновление токена
        path('books/', BookViewSet.as_view({'get': 'list', 'post': 'create'}), name='book_list'),  
        path('books/<int:pk>/', BookViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='book_detail'),
    ]
