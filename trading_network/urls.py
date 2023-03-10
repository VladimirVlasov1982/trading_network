from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("products/", include("provider.urls.product")),
    path("factories/", include("provider.urls.factory")),
    path("retail-networks/", include("provider.urls.retail_network")),
    path("individual-entrepreneurs/", include("provider.urls.individual_entrepreneur")),
    path("network-object/", include("provider.urls.network_object")),
]
