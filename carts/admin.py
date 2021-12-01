from django.contrib import admin

from carts.models import CartItem, Cart
from products.models import Product


admin.site.register(Cart)
admin.site.register(CartItem)
