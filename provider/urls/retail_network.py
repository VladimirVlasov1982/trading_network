from django.urls import path

from provider.views import RetailNetworkListCreateView, RetailNetworkRetrieveUpdateDestroyView

urlpatterns = [
    path("", RetailNetworkListCreateView.as_view(), name="retail-network-list-create"),
    path("<int:pk>", RetailNetworkRetrieveUpdateDestroyView.as_view(), name="retail-network-retrieve-update-destroy"),
]
