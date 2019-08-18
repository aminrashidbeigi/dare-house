from rest_framework import serializers

from django.contrib.auth.models import User
from warehouse.models import Segment, Order, Product

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'is_active', 'price', 'image')

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'customer', 'status', 'created_at')

class SegmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Segment
        fields = ('id', 'label')