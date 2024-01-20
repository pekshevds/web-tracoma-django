from django.contrib import admin
from warehouse_accounting_app.models import (
    Order,
    Cargo,
    Warehouse
)


@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ("__str__", 'id',)


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ("__str__", "order", 'id',)


class CargoInLine(admin.TabularInline):
    model = Cargo
    fields = ('name',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [CargoInLine]
    list_display = ("__str__", 'id',)
