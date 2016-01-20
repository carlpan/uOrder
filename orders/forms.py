from django import forms
from .models import Order

class CreateOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['current_location', 'arrival_time', 'instructions']
