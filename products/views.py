import os

import stripe
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from dotenv import load_dotenv

from products.models import Product

load_dotenv()
stripe.api_key = os.environ['STRIPE_SECRET_KEY']

products = stripe.Product.list()
prices = stripe.Price.list()


def sync_products_view(request):
    for prod in products.data:
        price_ = [p for p in prices.data if p.product == prod.id][0]
        price = float(price_.unit_amount / 100)
        print(price)

        obj, _ = Product.objects.get_or_create(name=prod.name)
        obj.price = price
        obj.active = prod.active
        obj.image = prod.images
        obj.save()
    return HttpResponse('data')
