from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from warehouse_app.models import (
    Warehouse,
    Cargo,
    Incoming,
    Outgoing,
    Moving
)
from warehouse_app.forms import WarehouseForm


class WarehouseView(View):
    def get(self, request, item_id: str):
        warehouse = get_object_or_404(Warehouse, pk=item_id)
        context = {
            "form": WarehouseForm(instance=warehouse),
            "item": warehouse
        }
        return render(request,
                      template_name="warehouse_app/warehouse.html",
                      context=context)

    def post(self, request, item_id: str):
        warehouse = get_object_or_404(Warehouse, pk=item_id)
        form = WarehouseForm(request.POST or None, instance=warehouse)
        if form.is_valid():
            form.save()
            return redirect('warehouse_app:show-warehouse-list-page')
        context = {
            "form": WarehouseForm(instance=warehouse),
            "item": warehouse
        }
        return render(request,
                      template_name="warehouse_app/warehouse.html",
                      context=context)


class WarehouseListView(View):
    def get(self, request):
        context = {
            "items": Warehouse.objects.all()
        }
        return render(request,
                      template_name="warehouse_app/warehouse_list.html",
                      context=context)


class CargoView(View):
    def get(self, request, item_id: str):
        print(item_id)
        return render(request,
                      template_name="warehouse_app/cargo.html")


class CargoListView(View):
    def get(self, request):
        context = {
            "items": Cargo.objects.all()
        }
        return render(request,
                      template_name="warehouse_app/cargo_list.html",
                      context=context)


class IncomingView(View):
    def get(self, request, item_id: str):
        print(item_id)
        return render(request,
                      template_name="warehouse_app/incoming.html")


class IncomingListView(View):
    def get(self, request):
        context = {
            "items": Incoming.objects.all()
        }
        return render(request,
                      template_name="warehouse_app/incoming_list.html",
                      context=context)


class OutgoingView(View):
    def get(self, request, item_id: str):
        print(item_id)
        return render(request,
                      template_name="warehouse_app/outgoing.html")


class OutgoingListView(View):
    def get(self, request):
        context = {
            "items": Outgoing.objects.all()
        }
        return render(request,
                      template_name="warehouse_app/outgoing_list.html",
                      context=context)


class MovingView(View):
    def get(self, request, item_id: str):
        print(item_id)
        return render(request,
                      template_name="warehouse_app/moving.html")


class MovingListView(View):
    def get(self, request):
        context = {
            "items": Moving.objects.all()
        }
        return render(request,
                      template_name="warehouse_app/moving_list.html",
                      context=context)
