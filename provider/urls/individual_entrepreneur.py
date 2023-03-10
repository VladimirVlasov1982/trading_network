from django.urls import path

from provider.views import IndividualEntrepreneurListCreateView, IndividualEntrepreneurRetrieveUpdateDestroyView

urlpatterns = [
    path("", IndividualEntrepreneurListCreateView.as_view(),
         name="individual_entrepreneur-list-create"),
    path("<int:pk>", IndividualEntrepreneurRetrieveUpdateDestroyView.as_view(),
         name="individual_entrepreneur-retrieve-update-destroy"),
]
