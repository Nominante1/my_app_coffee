from django.urls import path, include 
from rest_framework.routers import DefaultRouter
from .views import BookViewSet 
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import BookViewSet  # Ваши представления
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = DefaultRouter() 
router.register(r'books', BookViewSet) 

schema_view = get_schema_view(
    openapi.Info(
        title="API через Swagger",
        default_version='v1',
        description="Демонстрация Restfull API через Swagger",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="monitor81@mail.ru"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [ 
        path('api/', include(router.urls)), 
        path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Получение токена
        path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Обновление токена
        path('books/', BookViewSet.as_view({'get': 'list', 'post': 'create'}), name='book_list'),  
        path('books/<int:pk>/', BookViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='book_detail'),
        path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    ]
