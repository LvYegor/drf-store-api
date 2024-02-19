from django.urls import path
from .views import StoreListAPIView


urlpatterns = [
    path('Stores/', StoreListAPIView.as_view(), name='store-list')
]
