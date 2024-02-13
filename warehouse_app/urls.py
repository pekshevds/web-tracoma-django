from django.urls import path
from warehouse_app.views import (
    WarehouseListView,
    WarehouseView,
    CargoListView,
    CargoView,
    IncomingListView,
    IncomingView,
    OutgoingListView,
    OutgoingView,
    MovingListView,
    MovingView
)

app_name = 'warehouse_app'

urlpatterns = [
    path('catalogs/warehouse',
         WarehouseListView.as_view(), name='show-warehouse-list-page'),
    path('catalogs/warehouse/<str:item_id>',
         WarehouseView.as_view(), name='show-warehouse-edit-page'),
    path('catalogs/cargo',
         CargoListView.as_view(), name='show-cargo-list-page'),
    path('catalogs/cargo/<str:item_id>',
         CargoView.as_view(), name='show-cargo-edit-page'),
    path('docs/incoming',
         IncomingListView.as_view(), name='show-incoming-list-page'),
    path('docs/incoming/<str:item_id>',
         IncomingView.as_view(), name='show-incoming-edit-page'),
    path('docs/outgoing',
         OutgoingListView.as_view(), name='show-outgoing-list-page'),
    path('docs/outgoing/<str:item_id>',
         OutgoingView.as_view(), name='show-outgoing-edit-page'),
    path('docs/moving',
         MovingListView.as_view(), name='show-moving-list-page'),
    path('docs/moving/<str:item_id>',
         MovingView.as_view(), name='show-moving-edit-page'),
]
