from django.db import models
from django.utils.dateformat import format
from main_app.base import Document
from main_app.services import ganerate_new_number


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
