from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User
from warehouse.models import Order, Product, Segment
from rest_framework import routers
from warehouse.views import UserViewSet, ProductViewSet, OrderViewSet, CategoryViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
