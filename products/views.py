import os

import stripe
from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.views.generic import TemplateView
from django.conf import settings
from django.http import HttpResponse
from .models import Item

stripe.api_key = settings.STRIPE_SECRET_KEY


class ItemsListView(TemplateView):
    template_name = 'items_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = Item.objects.all()
        return context


class ItemPageView(TemplateView):
    template_name = 'item.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        item = get_object_or_404(Item, pk=context['id'])
        context['item'] = item
        return context


class CreateCheckoutSessionView(View):
    def get(self, request, *args, **kwargs):
        YOUR_DOMAIN = os.getenv('YOUR_DOMAIN')
        item_id = self.kwargs['id']
        item = get_object_or_404(Item, id=item_id)
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': item.price,
                        'product_data': {
                            'name': item.name,
                        }
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + 'success/',
            cancel_url=YOUR_DOMAIN + 'cancel/',
        )
        return redirect(checkout_session.url, code=303)


def show_succes(request):
    return HttpResponse('<h1>Покупка успешно совершена</h1>')


def show_cancel(request):
    return HttpResponse('<h1>Покупка отменена!</h1>')
