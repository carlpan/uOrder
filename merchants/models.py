from __future__ import unicode_literals
import datetime

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


# Custom function
def get_business_hour(merchant_id, weekday):
    format_string = '%I:%M%p'
    ohs = OpeningHours.objects.filter(merchant_id=merchant_id)
    from_hour = ohs.filter(weekday=weekday)[0].from_hour.strftime(format_string)
    to_hour = ohs.filter(weekday=weekday)[0].to_hour.strftime(format_string)
    return dict(from_hour=from_hour, to_hour=to_hour)

def is_open(merchant_id, now=None):
    if now is None:
        now = datetime.datetime.now()

    now_time = datetime.time(now.hour, now.minute)

    if merchant_id:
        ohs = OpeningHours.objects.filter(merchant__id=merchant_id)
    else:
        ohs = Merchant.objects.first().openinghours_set.all()

    opening = False
    for oh in ohs:
        # start and end is on the same day
        if oh.weekday == now.isoweekday() and oh.from_hour <= now_time and oh.to_hour >= now_time:
            opening = True

    return opening
