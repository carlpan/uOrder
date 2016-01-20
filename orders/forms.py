from django import forms
from .models import Order

ARRIVAL_TIMES = (
    (1, '20'),
    (2, '25'),
    (3, '30'),
    (4, '45'),
)

class CreateOrderForm(forms.ModelForm):
    current_location = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                                     'placeholder': 'Enter your current location.'}),
                                       required=False)
    arrival_time = forms.CharField(widget=forms.Select(attrs={'class': 'form-control'},
                                                       choices=ARRIVAL_TIMES), required=False)
    instructions = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control',
                    'placeholder': 'Special instructions for restaurants to your food preparation preferences'}),
                                   required=False)

    class Meta:
        model = Order
        fields = ['current_location', 'arrival_time', 'instructions']

