from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


order_statuses = (
    ('submitted', 'submitted'),
    ('picking', 'picking'),
    ('picked', 'picked')
)


class Category(models.Model):
    title = models.CharField(max_length=128)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=False)
    price = models.IntegerField(default=0)
    image = models.CharField(max_length=128, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


    def __str__(self):
        return self.title


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer')
    status = models.CharField(max_length=32, choices=order_statuses)
    products = models.ManyToManyField(Product, through='OrderProduct', blank=True)
    created_at = models.DateTimeField(default=timezone.now)


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('order', 'product'), )


class Segment(models.Model):
    label = models.CharField(max_length=32)
    products = models.ManyToManyField(Product, through='SegmentProduct')


class SegmentProduct(models.Model):
    segment = models.ForeignKey(Segment, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)

    class Meta:
        unique_together = (('segment', 'product'), )
