from django.urls import path, include
from rest_framework.routers import SimpleRouter

from provider.views import NetworkLinkViewSet

network_link_router = SimpleRouter()
network_link_router.register("network-link", NetworkLinkViewSet)

urlpatterns = [
    path("", include(network_link_router.urls)),
]
