from django.urls import include, URLPattern, URLResolver, reverse
from rest_framework.response import Response
from rest_framework import routers
from rest_framework.views import APIView

from api import urls


class NotSlowFoodAPI(routers.APIRootView):
    """API root """
    pass

class APIRouter(routers.DefaultRouter):
    APIRootView = NotSlowFoodAPI


class RootView(APIView):
    def get(self, request, *args, **kwargs):
        api_urls: list[dict[str, str]] = []

        for url in urls.urlpatterns:
            if isinstance(url, URLPattern):
                api_urls.append({
                    'name': url.name,
                    'url': request.build_absolute_uri(reverse(url.name))
                })
            elif isinstance(url, URLResolver):
                for url in url.url_patterns:
                    if not 'detail' in url.name:
                        api_urls.append({
                            'name': url.name,
                            'url': request.build_absolute_uri(reverse(url.name))
                        })
                
        return Response({ url['name']: url['url'] for url in api_urls})