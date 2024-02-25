from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StoresViewSet, StoreProductsViewSet

router = DefaultRouter()
router.register(r'stores', StoresViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('stores/<int:store_id>/products/', StoreProductsViewSet.as_view({'get': 'list', 'post': 'create'}), name='store-products'),
]

