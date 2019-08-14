from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from warehouse.serializers import UserSerializer, ProductSerializer, OrderSerializer, SegmentSerializer
from django.contrib.auth.models import User
from warehouse.models import Product, Order, Segment

# Create your views here.

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# ViewSets define the view behavior.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# ViewSets define the view behavior.
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer