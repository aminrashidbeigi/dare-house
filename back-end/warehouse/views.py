from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from warehouse.serializers import UserSerializer, ProductSerializer, OrderSerializer, SegmentSerializer, CategorySerializer
from django.contrib.auth.models import User
from warehouse.models import Product, Order, Segment, Category, OrderProduct, Placement
import json

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrdersViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class SegmentsViewSet(viewsets.ModelViewSet):
    queryset = Segment.objects.all()
    serializer_class = SegmentSerializer


class CategoryViewSet(viewsets.ViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class get_order_products(APIView):
    def get(self, request, order_id):
        print(order_id)
        print("dsadsads")
        return Response("dsadsa")
    # queryset = Category.objects.all()
    # serializer_class = CategorySerializer


class Actions(viewsets.ViewSet):
    queryset = Order.objects.all()

    def pick_order(self, request, order_id):
        order = Order.objects.filter(pk=order_id).first()
        if order.status == 'picked':
            return Response({
                'status': False
            })

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

    def submit_segment(self, request, segment_id):
        segment = Segment.objects.filter(pk=segment_id).first()
        product_ids = json.loads(request.body).get('products')

        for product in product_ids:
            placement = Placement.objects.filter(product_id=product).first()
            if placement is None:
                placement = Placement()
                product = Product.objects.get(pk=product)
                placement.product = product
                placement.segment = segment
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
