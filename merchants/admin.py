from django.contrib import admin
from .models import Merchant, OpeningHours

# Register your models here.
class MerchantAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
admin.site.register(Merchant, MerchantAdmin)

class OpeningHoursAdmin(admin.ModelAdmin):
    list_display = ['weekday', 'from_hour', 'to_hour']
    list_editable = ['weekday', 'from_hour', 'to_hour']
admin.site.register(OpeningHours, OpeningHoursAdmin)