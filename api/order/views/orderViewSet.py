from rest_framework.viewsets import ModelViewSet
from api.order.serializers import OrderSerializer
from apps.order.models import Order

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer