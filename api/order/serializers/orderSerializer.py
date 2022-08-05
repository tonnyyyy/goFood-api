from rest_framework.serializers import ModelSerializer
from apps.order.models import Order

class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
