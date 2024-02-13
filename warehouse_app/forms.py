from django.forms import ModelForm
from warehouse_app.models import Warehouse


class WarehouseForm(ModelForm):

    class Meta:
        model = Warehouse
        fields = ['name', 'type']
