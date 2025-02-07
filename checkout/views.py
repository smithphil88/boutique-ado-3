from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "there's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51QooOMRjieCP17KFbuTCA3VF7R2eVtbixeZ0Pq3ON783eUI7drvH8uQ2WgblAUjkEggqXYsRsZzCkOLZYpJrlb2t00ffO1b46h',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
