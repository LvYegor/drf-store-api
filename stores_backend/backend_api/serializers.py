from rest_framework import serializers
from .models import *


class StoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductComment
        fields = '__all__'
