from django import forms
from django.contrib import admin
from .models import Category, Product, Segment, Order, Placement, OrderProduct


class PlacementInline(admin.TabularInline):
    model = Placement
    extra = 1


class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    extra = 1


class SegmentAdmin(admin.ModelAdmin):
    inlines = (PlacementInline,)


class ProductAdmin(admin.ModelAdmin):
    inlines = (PlacementInline,)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderProductInline,)


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Segment, SegmentAdmin)
admin.site.register(Order, OrderAdmin)
