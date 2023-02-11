from django.urls import path
from .views import ItemListView, ItemDetailView

urlpatterns = [
    path('', ItemListView.as_view(), name='list-item'),
    path('item/<pk>', ItemDetailView.as_view(), name='item-detail')
]
