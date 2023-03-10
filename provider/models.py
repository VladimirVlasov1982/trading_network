from django.db import models


class Contact(models.Model):
    email = models.EmailField()
    country = models.CharField(max_length=255, verbose_name="Страна")
    city = models.CharField(max_length=255, verbose_name="Город")
    street = models.CharField(max_length=255, verbose_name="Улица")
    house_number = models.IntegerField(verbose_name="Номер дома")


class NetworkObject(Contact):
    name = models.CharField(max_length=255, verbose_name="Название")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")

    objects = models.Manager()

    class Meta:
        verbose_name = "Объект сети"
        verbose_name_plural = "Объекты сети"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Наименование")
    model = models.CharField(max_length=255, verbose_name="Модель")
    release_date = models.DateField(verbose_name="Дата выхода")
    supplier = models.ForeignKey(NetworkObject, on_delete=models.CASCADE, verbose_name="Поставщик",
                                 null=True, blank=True, related_name='products')

    objects = models.Manager()

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.name


class Factory(NetworkObject):
    objects = models.Manager()

    class Meta:
        verbose_name = "Завод"
        verbose_name_plural = "Заводы"

    def __str__(self):
        return self.name


class RetailNetwork(NetworkObject):
    supplier = models.ForeignKey(Factory, on_delete=models.CASCADE, verbose_name="Поставщик")
    debt = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Задолженность перед поставщиком",
                               null=True, blank=True)

    objects = models.Manager()

    class Meta:
        verbose_name = "Розничная сеть"
        verbose_name_plural = "Розничные сети"

    def __str__(self):
        return self.name


class IndividualEntrepreneur(NetworkObject):
    supplier = models.ForeignKey(RetailNetwork, on_delete=models.CASCADE,  verbose_name="Поставщик")
    debt = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Задолженность перед поставщиком",
                               null=True, blank=True)

    objects = models.Manager()

    class Meta:
        verbose_name = "Индивидуальный предприниматель"
        verbose_name_plural = "Индивидуальные предприниматели"

    def __str__(self):
        return self.name
