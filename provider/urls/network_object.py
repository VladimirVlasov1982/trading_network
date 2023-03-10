from django.urls import path

from provider.views import NetworkObjectListCreateView , NetworkObjectRetrieveUpdateDestroyView

urlpatterns = [
    path("", NetworkObjectListCreateView.as_view(), name="network-object-list-create"),
    path("<int:pk>", NetworkObjectRetrieveUpdateDestroyView.as_view(), name="network-object-retrieve-update-destroy"),
]