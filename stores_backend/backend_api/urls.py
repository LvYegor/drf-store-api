from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StoresViewSet, StoreProductsViewSet, ProductsViewSet

router = DefaultRouter(trailing_slash=True)
router.register(r'stores', StoresViewSet)
router.register(r'products', ProductsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('stores/<int:store_id>/products/', StoreProductsViewSet.as_view({'get': 'list'})),
]
