from rest_framework import routers
from api.restaurant.views import RestaurantViewSet

restaurant_router = routers.DefaultRouter()

restaurant_router.register('', RestaurantViewSet, basename="restaurant")