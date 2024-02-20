from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StoresViewSet

router = DefaultRouter()
router.register(r'stores', StoresViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
