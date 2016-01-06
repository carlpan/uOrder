from __future__ import unicode_literals

from django.db import models

# Create your models here.

WEEKDAYS = (
    (1, "Monday"),
    (2, "Tuesday"),
    (3, "Wednesday"),
    (4, "Thursday"),
    (5, "Friday"),
    (6, "Saturday"),
    (7, "Sunday"),
)

class Merchant(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Merchant'
        verbose_name_plural = 'Merchants'

    def __str__(self):
        return "%s (%s)" % (self.name, self.description)



class OpeningHours(models.Model):
    merchant = models.ForeignKey(Merchant)
    weekday = models.IntegerField(choices=WEEKDAYS)
    from_hour = models.TimeField()
    to_hour = models.TimeField()

    def __str__(self):
        return "%s %s (%s - %s)" % (self.merchant, self.weekday, self.from_hour, self.to_hour)