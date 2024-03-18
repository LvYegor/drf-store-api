from rest_framework import viewsets, filters, mixins
from django_filters.rest_framework import DjangoFilterBackend

from .models import Store, Product, ProductComment
from .serializers import StoresSerializer, ProductSerializer, CommentSerializer


class StoresViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    queryset = Store.objects.all()
    serializer_class = StoresSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name', 'address', '=floor_area']


class StoreProductsViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['name', '=price', 'specs', '=rating', 'supplier_info', 'made_in', 'production_company_name']
    ordering_fields = ['name', 'price', 'specs', 'rating', 'supplier_info', 'made_in', 'production_company_name']
    filterset_fields = ['status']

    def get_queryset(self):
        store_id = self.kwargs['store_id']
        queryset = Product.objects.select_related('store').filter(store_id=store_id)

        return queryset


class ProductsViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCommentsViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = CommentSerializer

    def get_queryset(self):
        product_id = self.kwargs['product_id']
        queryset = ProductComment.objects.select_related('product').filter(product_id=product_id)

        return queryset


class CommentsViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet
):
    queryset = ProductComment.objects.all()
    serializer_class = CommentSerializer
