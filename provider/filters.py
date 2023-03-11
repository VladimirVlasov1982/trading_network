import django_filters

from provider.models import NetworkLink


class NetworkLinkFilter(django_filters.rest_framework.FilterSet):
    """
    Фильтрация объектов NetworkLink по определенной стране
    """
    country = django_filters.CharFilter(field_name="contact_link__country", lookup_expr="icontains", )

    class Meta:
        model = NetworkLink
        fields = ("contact_link__country",)
