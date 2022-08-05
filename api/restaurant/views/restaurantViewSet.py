from rest_framework.viewsets import ModelViewSet

from apps.restaurant.models import Restaurant
from api.restaurant.serializers import RestaurantSerializer

class RestaurantViewSet(ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer