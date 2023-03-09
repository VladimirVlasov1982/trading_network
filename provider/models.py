from django.db import models


class NetworkObject(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    house_number = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Объект сети"
        verbose_name_plural = "Объекты сети"


class Product(models.Model):
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    release_date = models.DateField()
    supplier = models.ForeignKey(NetworkObject, on_delete=models.CASCADE)
    debt = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class Factory(NetworkObject):
    class Meta:
        verbose_name = "Завод"
        verbose_name_plural = "Заводы"


class RetailNetwork(NetworkObject):
    retail_factory = models.ForeignKey(Factory, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Розничная сеть"
        verbose_name_plural = "Розничные сети"


class IndividualEntrepreneur(NetworkObject):
    retail_network = models.ForeignKey(RetailNetwork, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Индивидуальный предприниматель"
        verbose_name_plural = "Индивидуальные предприниматели"
