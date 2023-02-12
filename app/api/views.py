from django.http import JsonResponse
from django.views.generic import ListView, DetailView, View
from django.conf import settings
from .models import Item
import stripe


class ItemListView(ListView):
    """
    Returns the list of volumes of an item.
    """
    model = Item


class ItemDetailView(DetailView):
    """
    Returns an item by id.
    """
    model = Item


class ItemBuyView(View):
    """
    Returns session id for Stripe by item id.
    """
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        item = Item.objects.get(pk=pk)

        session = stripe.checkout.Session.create(
            api_key=settings.STRIPE_API_KEY,
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': item.name,
                    },
                    'unit_amount': int(item.price * 100),
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=request.headers.get('Referer'),
            cancel_url=request.headers.get('Referer'),
        )

        return JsonResponse({'session_id': session.get('id')})
