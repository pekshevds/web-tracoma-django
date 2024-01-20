from django.db import models
from django.utils.dateformat import format
from main_app.base import Directory, Document
from order_app.models import Order
from main_app.services import ganerate_new_number


class Warehouse(Directory):

    CA = "CA"
    WH = "WH"
    EM = "WH"
    TYPES_OF_WAREHOUSE = [
        (CA, "Контрагент (юридическое лицо, сторонний контрагент, подрядчик)"),
        (WH, "Склад (адрес, помещение)"),
        (EM, "Сотрудник (курьер, экспедитор)"),
    ]

    type = models.CharField(verbose_name="Тип", max_length=2,
                            choices=TYPES_OF_WAREHOUSE, default=WH)

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
    recipient = models.ForeignKey(
        Warehouse, on_delete=models.PROTECT, verbose_name="Получатель",
        null=True, blank=True)

    def save(self, *args, **kwargs) -> None:
        if not self.number:
            self.number = ganerate_new_number(model=Incoming)
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"Приходный ордер №{self.number} от {format(self.date, 'd F Y')}"

    class Meta:
        verbose_name = "Приходный ордер"
        verbose_name_plural = "Приходные ордера"
        ordering = ["-number"]


class IncomingItem(models.Model):
    incoming = models.ForeignKey(Incoming, on_delete=models.PROTECT)
    cargo = models.ForeignKey(Cargo, on_delete=models.PROTECT)


class Outgoing(Document):

    sender = models.ForeignKey(
        Warehouse, on_delete=models.PROTECT, verbose_name="Отправитель",
        null=True, blank=True)

    def save(self, *args, **kwargs) -> None:
        if not self.number:
            self.number = ganerate_new_number(model=Outgoing)
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"Расходный ордер №{self.number} от {format(self.date, 'd F Y')}"

    class Meta:
        verbose_name = "Расходный ордер"
        verbose_name_plural = "Расходные ордера"
        ordering = ["-number"]


class OutgoingItem(models.Model):
    outgoing = models.ForeignKey(Outgoing, on_delete=models.PROTECT)
    cargo = models.ForeignKey(Cargo, on_delete=models.PROTECT)


class Moving(Document):

    sender = models.ForeignKey(
        Warehouse, on_delete=models.PROTECT,
        verbose_name="Отправитель", related_name="sender",
        null=True, blank=True)
    recipient = models.ForeignKey(
        Warehouse, on_delete=models.PROTECT,
        verbose_name="Получатель", related_name="recipient",
        null=True, blank=True)

    def save(self, *args, **kwargs) -> None:
        if not self.number:
            self.number = ganerate_new_number(model=Moving)
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"Перемещение №{self.number} от {format(self.date, 'd F Y')}"

    class Meta:
        verbose_name = "Перемещение"
        verbose_name_plural = "Перемещения"
        ordering = ["-number"]


class MovingItem(models.Model):
    moving = models.ForeignKey(Moving, on_delete=models.PROTECT)
    cargo = models.ForeignKey(Cargo, on_delete=models.PROTECT)
