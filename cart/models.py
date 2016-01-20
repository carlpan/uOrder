from __future__ import unicode_literals

from django.db import models
from menu.models import MenuItem
from merchants.models import Merchant
from django.contrib.auth.models import User
from django.http import Http404

# Create your models here.

class Cart(models.Model):
    user = models.OneToOneField(User, null=True, blank=True)
    merchant = models.OneToOneField(Merchant, null=True, blank=True)
    creation_date = models.DateTimeField()
    checked_out = models.BooleanField(default=False)
    #total = models.DecimalField(default=0.00, max_digits=6, decimal_places=2)

    class Meta:
        verbose_name = 'cart'
        verbose_name_plural = 'carts'

    def __unicode__(self):
        return unicode(self.creation_date)

    def save(self, *args, **kwargs):
        self.calculate_cart()
        super(Cart, self).save(*args, **kwargs)

    def get_cart_items(self):
        return self.cartitem_set.all()

    def size(self):
        return len(self.get_cart_items())

    def aggregate_cart_size(self):
        count = 0
        for cartitem in self.get_cart_items():
            count += cartitem.quantity
        return count

    def create_or_update_cart_item(self, menuitem_pk, quantity=None):
        menu_item = MenuItem.objects.get(pk=menuitem_pk)
        cartitem, created = CartItem.objects.get_or_create(cart=self, menu_item=menu_item, quantity=quantity)

        # if cartitem already existed, update its quantity
        if not created:
            new_quantity = cartitem.quantity + int(quantity)
            cartitem.quantity = new_quantity
            cartitem.save()

    def retrieve_cart_item(self, cartitem_id):
        try:
            cartitem = CartItem.objects.get(cart=self, id=cartitem_id)
        except CartItem.DoesNotExist:
            raise Http404
        return cartitem

    def calculate_cart(self):
        total = 0
        for item in self.get_cart_items():
            total += item.get_total_price()
        return total

    def empty_cart(self):
        if self.id:
            self.cartitem_set.all().delete()
            self.delete()


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

    def update_quantity(self, quantity):
        self.quantity = quantity
        self.save()
