from django.urls import path, include 
from rest_framework.routers import DefaultRouter
#from .views import BookViewSet 
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import ProductViewSet 
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

#router = DefaultRouter() 
#router.register(r'books', BookViewSet) #создание маршрутов для стандартных операций

router1 = DefaultRouter()
router1.register(r'products', ProductViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title = "API для взаимодействия со базой данных склада",
        default_version='v1',
        description="Смогли)"
    ),
    public=True,
    permission_classes=(permissions.AllowAny,)#доступ для всех
)


urlpatterns = [
        path('api/', include(router1.urls)), #после api должен быть books/products
        path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Получение токена
        path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Обновление токена
        #path('books/', BookViewSet.as_view({'get': 'list', 'post': 'create'}), name='book_list'),  
        #path('books/<int:pk>/', BookViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='book_detail'),
        path('products/', ProductViewSet.as_view({'get': 'list', 'post': 'create'}), name='product_list'),
        path('products/<int:pk>/', ProductViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='product_detail'),
        path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    ]
