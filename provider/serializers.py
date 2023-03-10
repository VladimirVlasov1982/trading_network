from rest_framework import serializers

from provider.models import Product, Factory, RetailNetwork, IndividualEntrepreneur, NetworkObject


class NetworkObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = NetworkObject
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class FactorySerializer(serializers.ModelSerializer):
    products = serializers.SlugRelatedField(
        required=False,
        queryset=Product.objects.all(),
        slug_field="name",
        many=True
    )

    class Meta:
        model = Factory
        fields = ('id', 'name', 'country', 'city', 'street', 'house_number', 'created_at', 'products')


class RetailNetworkSerializer(serializers.ModelSerializer):
    retail_factory = serializers.SlugRelatedField(
        required=False,
        queryset=NetworkObject.objects.all(),
        slug_field="name",
    )
    products = serializers.SlugRelatedField(
        required=False,
        queryset=Product.objects.all(),
        slug_field="name",
        many=True
    )

    class Meta:
        model = RetailNetwork
        fields = '__all__'


class IndividualEntrepreneurSerializer(serializers.ModelSerializer):
    retail_network = serializers.SlugRelatedField(
        required=False,
        queryset=NetworkObject.objects.all(),
        slug_field="name",
    )
    products = serializers.SlugRelatedField(
        required=False,
        queryset=Product.objects.all(),
        slug_field="name",
        many=True
    )

    class Meta:
        model = IndividualEntrepreneur
        fields = '__all__'
