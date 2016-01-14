from django import forms
from django.core.exceptions import ValidationError

class UpdateItemQuantityForm(forms.Form):
    cartitem = forms.IntegerField(required=True)
    quantity = forms.IntegerField(required=True)

    def clean_quantity(self):
        quantity_data = self.cleaned_data['quantity']
        if quantity_data <= 0:
            raise ValidationError("Please enter a positive quantity.")
        return quantity_data
