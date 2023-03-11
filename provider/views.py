from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from provider.filters import NetworkLinkFilter
from provider.models import NetworkLink
from provider.permissions import IsActiveEmployee
from provider.serializers import NetworkLinkSerializer, NetworkLinkDetailSerializer


class NetworkLinkViewSet(viewsets.ModelViewSet):
    """Содержит в себе все базовые API-методы для торговой сети"""
    queryset = NetworkLink.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = NetworkLinkFilter
    default_serializer = NetworkLinkSerializer
    serializer_classes = {
        'retrieve': NetworkLinkDetailSerializer,
    }
    default_permission = [AllowAny()]
    permissions = {
        'update': [IsActiveEmployee()],
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer)

    def get_permissions(self):
        return self.permissions.get(self.action, self.default_permission)
