from django.urls import path

from provider.views import FactoryListCreateView, FactoryRetrieveUpdateDestroyView

urlpatterns = [
    path("", FactoryListCreateView.as_view(), name="factory-list-create"),
    path("<int:pk>", FactoryRetrieveUpdateDestroyView.as_view(), name="factory-retrieve-update-destroy"),
]
