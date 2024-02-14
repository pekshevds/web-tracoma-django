from django.forms import ModelForm, TextInput, NumberInput, Select
from warehouse_app.models import (
    Warehouse,
    Cargo
)


class WarehouseForm(ModelForm):

    class Meta:
        model = Warehouse
        fields = ['name', 'type']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'type': 'text'}),
            'type': Select(attrs={'class': 'form-control', 'type': 'text'}),
        }


class CargoForm(ModelForm):

    class Meta:
        model = Cargo
        fields = ['name', 'order', 'width', 'height', 'length',
                  'weight', 'volume', 'description']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'type': 'text'}),
            'order': Select(attrs={'class': 'form-control', 'type': 'text'}),
            'width': NumberInput(attrs={'class': 'form-control', 'type': 'number'}),
            'height': NumberInput(attrs={'class': 'form-control', 'type': 'number'}),
            'length': NumberInput(attrs={'class': 'form-control', 'type': 'number'}),
            'weight': NumberInput(attrs={'class': 'form-control', 'type': 'number'}),
            'volume': NumberInput(attrs={'class': 'form-control', 'type': 'number'}),
            'description': TextInput(attrs={'class': 'form-control', 'type': 'text'}),
        }
