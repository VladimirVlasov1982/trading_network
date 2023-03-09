from django.contrib import admin

from provider.models import NetworkObject, Product, IndividualEntrepreneur, Factory, RetailNetwork

admin.site.register(NetworkObject)
admin.site.register(Product)
admin.site.register(Factory)
admin.site.register(RetailNetwork)
admin.site.register(IndividualEntrepreneur)
