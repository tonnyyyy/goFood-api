from rest_framework.viewsets import ModelViewSet
from api.order.serializers import CategorySerializer
from apps.order.models import Category

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer