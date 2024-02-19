from rest_framework import generics
from .models import Store
from .serializers import StoresSerializer


class StoreListAPIView(generics.ListAPIView):
    queryset = Store.objects.all()
    serializer_class = StoresSerializer