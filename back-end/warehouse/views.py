from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from warehouse.serializers import UserSerializer, ProductSerializer, OrderSerializer, SegmentSerializer, CategorySerializer
from django.contrib.auth.models import User
from warehouse.models import Product, Order, Segment, Category

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer