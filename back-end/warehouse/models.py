from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


order_statuses = (
    ('submitted', 'submitted'),
    ('picking', 'picking'),
    ('picked', 'picked')
)


class Product(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(default='')
    is_active = models.BooleanField(default=False)
    price = models.IntegerField(default=0)
    image = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer')
    created_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=32, choices=order_statuses)


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Segment(models.Model):
    label = models.CharField(max_length=32)


class SegmentProduct(models.Model):
    segment = models.ForeignKey(Segment, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)
