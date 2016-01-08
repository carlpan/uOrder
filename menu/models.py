from __future__ import unicode_literals

from django.db import models

from merchants.models import Merchant

# Create your models here.

class MenuCategory(models.Model):
    name = models.CharField(max_length=100)
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    menu_category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE, null=True)
    entry_name = models.CharField(max_length=128)
    entry_description = models.CharField(max_length=200)
    entry_price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
         return "%s (%s) $%s" % (self.entry_name, self.entry_description, self.entry_price)

