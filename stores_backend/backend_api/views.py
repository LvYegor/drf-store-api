from rest_framework import viewsets, filters, mixins
from django_filters.rest_framework import DjangoFilterBackend
from .models import Store
from .serializers import StoresSerializer


class StoresViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet
):
    queryset = Store.objects.all()
    serializer_class = StoresSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name', 'address', 'floor_area']
