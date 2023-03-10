from rest_framework import generics

from provider.models import Product, Factory, RetailNetwork, IndividualEntrepreneur, NetworkObject
from provider.serializers import ProductSerializer, FactorySerializer, RetailNetworkSerializer, \
    IndividualEntrepreneurSerializer, NetworkObjectSerializer


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class FactoryListCreateView(generics.ListCreateAPIView):
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer


class FactoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer


class RetailNetworkListCreateView(generics.ListCreateAPIView):
    queryset = RetailNetwork.objects.all()
    serializer_class = RetailNetworkSerializer


class RetailNetworkRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RetailNetwork.objects.all()
    serializer_class = RetailNetworkSerializer


class IndividualEntrepreneurListCreateView(generics.ListCreateAPIView):
    queryset = IndividualEntrepreneur.objects.all()
    serializer_class = IndividualEntrepreneurSerializer


class IndividualEntrepreneurRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = IndividualEntrepreneur.objects.all()
    serializer_class = IndividualEntrepreneurSerializer


class NetworkObjectListCreateView(generics.ListCreateAPIView):
    queryset = NetworkObject.objects.all()
    serializer_class = NetworkObjectSerializer


class NetworkObjectRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = NetworkObject.objects.all()
    serializer_class = NetworkObjectSerializer
