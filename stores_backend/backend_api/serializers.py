from rest_framework import serializers
from .models import *
from django.utils.timezone import now


class StoresSerializer(serializers.ModelSerializer):
    store_lifetime = serializers.SerializerMethodField()

    class Meta:
        model = Store
        fields = '__all__'

    def get_store_lifetime(self, obj):
        return (now().date() - obj.established).days


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    comment_lifetime = serializers.SerializerMethodField()

    class Meta:
        model = ProductComment
        fields = '__all__'

    def get_comment_lifetime(self, obj):

        return (now() - obj.posted).days
