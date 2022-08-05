from rest_framework import routers
from api.order.views import OrderViewSet, CategoryViewSet

order_router = routers.DefaultRouter()

order_router.register('order', OrderViewSet, basename="order")
order_router.register('category', CategoryViewSet, basename="category")