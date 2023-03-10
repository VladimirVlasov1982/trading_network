from django.contrib import admin
from provider.models import NetworkObject, Product, IndividualEntrepreneur, Factory, RetailNetwork


@admin.register(NetworkObject)
class NetworkObjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'supplier_name', 'city')
    search_fields = ('name',)
    list_filter = ('city',)

    def has_add_permission(self, request):
        return False

    def supplier_name(self, obj):
        return obj.products.name

    supplier_name.short_description = "Поставщик"


@admin.register(RetailNetwork)
class RetailNetworkAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Product)
admin.site.register(Factory)
admin.site.register(IndividualEntrepreneur)
