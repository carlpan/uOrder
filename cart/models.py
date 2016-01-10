from __future__ import unicode_literals

from django.db import models
from menu.models import MenuItem
from django.contrib.auth.models import User

# Create your models here.

class Cart(models.Model):
    creation_date = models.DateTimeField()
    checked_out = models.BooleanField(default=False)
    total = models.DecimalField(default=0.00, max_digits=6, decimal_places=2)

    class Meta:
        verbose_name = 'cart'
        verbose_name_plural = 'carts'

    def __str__(self):
        return self.creation_date

    def get_cart_items(self):
        return self.cartitem_set.all()

    def size(self):
        return len(self.get_cart_items())

    def calculate_cart(self):
        total = 0
        cart_items = self.get_cart_items()
        for item in cart_items:
            total += item.get_total_price()
        self.total = total



class CartItem(models.Model):
    menu_item = models.ForeignKey(MenuItem)
    cart = models.ForeignKey(Cart)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = 'item'
        verbose_name_plural = 'items'
        ordering = ('cart',)

    def __str__(self):
        return "%d units of %s" % (self.quantity, self.menu_item.entry_name)

    def get_total_price(self):
        return self.quantity * self.menu_item.entry_price
