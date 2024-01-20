from django.db import models
from django.utils.dateformat import format
from main_app.base import Directory, Document
from warehouse_accounting_app.services import ganerate_new_number


class Order(Document):

    def save(self, *args, **kwargs) -> None:
        if not self.number:
            self.number = ganerate_new_number(model=Order)
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"Заказ №{self.number} от {format(self.date, 'd F Y')}"

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
        ordering = ["-number"]


class Warehouse(Directory):
    class Meta:
        verbose_name = "Место хранения"
        verbose_name_plural = "Места хранения"


class Cargo(Directory):
    order = models.ForeignKey(
        Order, related_name="cargoes", on_delete=models.PROTECT,
        verbose_name="Заказ")
    width = models.DecimalField(
        verbose_name="Ширина, см", max_digits=15, decimal_places=3)
    height = models.DecimalField(
        verbose_name="Высота, см", max_digits=15, decimal_places=3)
    length = models.DecimalField(
        verbose_name="Длина, см", max_digits=15, decimal_places=3)
    weight = models.DecimalField(
        verbose_name="Вес, кг", max_digits=15, decimal_places=3)
    volume = models.DecimalField(
        verbose_name="Объем, м3", max_digits=15, decimal_places=5)
    description = models.CharField(verbose_name="Описание", max_length=150)

    class Meta:
        verbose_name = "Груз"
        verbose_name_plural = "Грузы"


class Incoming(Document):
    pass


class IncomingItem(Document):
    incoming = models.ForeignKey(Incoming, on_delete=models.PROTECT)
    cargo = models.ForeignKey(Cargo, on_delete=models.PROTECT)


class Outgoing(Document):
    pass


class OutgoingItem(Document):
    outgoing = models.ForeignKey(Outgoing, on_delete=models.PROTECT)
    cargo = models.ForeignKey(Cargo, on_delete=models.PROTECT)


class Moving(Document):
    pass


class MovingItem(Document):
    moving = models.ForeignKey(Moving, on_delete=models.PROTECT)
    cargo = models.ForeignKey(Cargo, on_delete=models.PROTECT)
