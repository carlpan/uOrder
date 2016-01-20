from __future__ import unicode_literals

from django.db import models
from cart.models import Cart, CartItem
from merchants.models import Merchant
from authen.models import UserProfile
from menu.models import MenuItem

# Create your models here.

ARRIVAL_TIMES = (
    (1, '10'),
    (2, '15'),
    (3, '20'),
)

class Order(models.Model):
    customer = models.OneToOneField(UserProfile, null=True, blank=True)
    merchant = models.OneToOneField(Merchant, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    current_location = models.CharField(max_length=100, null=True, blank=True)
    arrival_time = models.TimeField(max_length=3, choices=ARRIVAL_TIMES, null=True, blank=True)
    instructions = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        ordering = ('-created',)

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_username(self):
        return self.customer.user.username

    def get_firstname(self):
        firstname = self.customer.user.first_name
        if not firstname:
            return self.get_username()
        return firstname

    def get_lastname(self):
        return self.customer.user.last_name

    def get_customer_email(self):
        return self.customer.user.email

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.orderitem_set.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order)
    menu_item = models.ForeignKey(MenuItem)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity