from django.contrib import admin
from order_app.models import Order
from warehouse_app.admin import CargoInLine


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [CargoInLine]
    list_display = ("__str__", 'id',)
