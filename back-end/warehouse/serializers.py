from rest_framework import serializers

from django.contrib.auth.models import User
from warehouse.models import Segment, Order, Product, Category


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    segments = serializers.StringRelatedField(many=True)
    category = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'is_active', 'price', 'image', 'category', 'segments')


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    customer = serializers.StringRelatedField()
    products = ProductSerializer(many=True)

    class Meta:
        model = Order
        fields = ('id', 'customer', 'status', 'products', 'created_at')


class SegmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Segment
        fields = ('id', 'label')


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'parent', 'is_active')
