from django.urls import path
from .views import ItemListView, ItemDetailView, ItemBuyView

urlpatterns = [
    path('', ItemListView.as_view(), name='list-item'),
    path('item/<pk>', ItemDetailView.as_view(), name='item-detail'),
    path('buy/<pk>', ItemBuyView.as_view(), name='buy-item'),
]
