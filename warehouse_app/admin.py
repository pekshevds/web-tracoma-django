from django.contrib import admin
from warehouse_app.models import (
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
