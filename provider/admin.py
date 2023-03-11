from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from provider.models import Product, IndividualEntrepreneur, Factory, NetworkLink, Contact, NetworkObject, RetailNetwork


@admin.action(description="Очистить задолженность перед поставщиком у выбранных объектов")
def debt_reset(modeladmin, requset, queryset):
    queryset.update(debt=0)


@admin.register(NetworkLink)
class RetailNetworkAdmin(admin.ModelAdmin):
    list_display = ('name', 'provider_link_object', 'contact_link')
    list_filter = ('contact_link__city',)
    actions = [debt_reset]

    def provider_link_object(self, obj):
        url = reverse('admin:provider_networkobject_change', args=[obj.provider_link.id])
        return mark_safe(f'<a href="{url}">{obj.provider_link.name}</a>')

    provider_link_object.short_description = "Поставщик"


admin.site.register(Product)
admin.site.register(Factory)
admin.site.register(IndividualEntrepreneur)
admin.site.register(Contact)
admin.site.register(NetworkObject)
admin.site.register(RetailNetwork)
