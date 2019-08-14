from rest_framework import serializers

from django.contrib.auth.models import User
from warehouse.models import Segment, Order, Product

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# Serializers define the API representation.
class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('id','title', 'ticket_id','user', 'content', 'category','created', 'modified')

# Serializers define the API representation.
class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ('name', 'slug')

# Serializers define the API representation.
class SegmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Segment
        fields = ('name', 'slug')