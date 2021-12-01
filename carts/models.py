from django.contrib.auth.models import User
from django.db import models

from products.models import Product


class CartAbstract(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class CartItem(CartAbstract):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.product.name}-{self.quantity}"


class Cart(CartAbstract):
    items = models.ManyToManyField(CartItem)
    total_items = models.PositiveIntegerField(default=0)
    total_price = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.user.username} - id:{self.id}"
