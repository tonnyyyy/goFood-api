from django.urls import include, path
from api.restaurant.routes import restaurant_router
from api.order.routes import order_router

from api.views import RootView, APIRouter

namespace = 'api'

api_root = APIRouter()

urlpatterns = [
    path('', RootView.as_view(), name='root'),
    path('restaurant/', include(restaurant_router.urls)),
    path('order/', include(order_router.urls)),
]


