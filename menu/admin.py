from django.contrib import admin
from .models import MenuCategory, MenuItem

# Register your models here.
class MenuCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(MenuCategory, MenuCategoryAdmin)

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['entry_name', 'entry_description', 'entry_price']
admin.site.register(MenuItem, MenuItemAdmin)