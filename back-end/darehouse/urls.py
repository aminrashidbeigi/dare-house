from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User
from warehouse.models import Order, Product, Segment
from rest_framework import routers
from warehouse.views import UserViewSet, ProductViewSet, OrdersViewSet, CategoryViewSet, Actions, OrderProductViewSet,\
    SegmentsViewSet

admin.site.site_header = "Warehouse Admin"
admin.site.site_title = "Warehouse Admin Panel"
admin.site.index_title = "Welcome to Warehouse Panel"

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'orders', OrdersViewSet)
router.register(r'segments', SegmentsViewSet)
router.register(r'orders\/(?P<order_id>[0-9]+)\/hello', OrdersViewSet)


urlpatterns = [
    path('', include('django_prometheus.urls')),
    path('jet/', include('jet.urls', 'jet')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/pick-order/<int:order_id>', Actions.as_view({'get': 'pick_order'}), name='pick_order'),
    path('api/submit-segment/<int:segment_id>', Actions.as_view({'post': 'submit_segment'}), name='submit_segment'),
    path('api/order-products/<int:order_id>', OrderProductViewSet.as_view({'get': 'order_products'}), name='order_products'),
]
