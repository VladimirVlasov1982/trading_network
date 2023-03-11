from rest_framework import serializers
from provider.models import Product, Contact, NetworkLink


class ContactSerializer(serializers.ModelSerializer):
    """
    Сериализатор контактов
    """

    class Meta:
        model = Contact
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    """
    Сериализатор продуктов
    """

    class Meta:
        model = Product
        fields = '__all__'


class NetworkLinkSerializer(serializers.ModelSerializer):
    """
    Сериализатор торговой сети
    """

    class Meta:
        model = NetworkLink
        fields = '__all__'


class NetworkLinkDetailSerializer(serializers.ModelSerializer):
    """
    Сериализатор детальной информации торговой сети
    """
    contact_link = ContactSerializer()
    products = ProductSerializer(many=True)
    provider_link = serializers.SlugRelatedField(
        queryset=NetworkLink.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = NetworkLink
        fields = '__all__'
        read_only_fields = ('debt',)
