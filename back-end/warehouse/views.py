from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from warehouse.serializers import UserSerializer, ProductSerializer, OrderSerializer, SegmentSerializer, CategorySerializer
from django.contrib.auth.models import User
from warehouse.models import Product, Order, Segment, Category, OrderProduct, Placement


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrdersViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.filter(status='submitted')
    serializer_class = OrderSerializer


class CategoryViewSet(viewsets.ViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)


class get_order_products(APIView):
    def get(self, request, order_id):
        print(order_id)
        print("dsadsads")
        return Response("dsadsa")
    # queryset = Category.objects.all()
    # serializer_class = CategorySerializer


class PickOrder(viewsets.ViewSet):
    queryset = Order.objects.all()

    def pick_order(self, request, order_id):
        order = Order.objects.filter(pk=order_id).first()
        order.status = 'picked'
        order.save()

        order_products = OrderProduct.objects.filter(order_id=order_id).all()
        for order_product in order_products:
            placement = Placement.objects.get(product_id=order_product.product_id)
            placement.count -= order_product.count
            placement.save()

        return Response({
            'status': True
        })


class OrderProductViewSet(viewsets.ViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def order_products(self, request, order_id):
        order = Order.objects.filter(pk=order_id)
        return Response(OrderSerializer(order, many=True, context={'request': request}).data)
