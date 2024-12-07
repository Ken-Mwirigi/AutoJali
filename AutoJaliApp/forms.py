# forms.py
from django import forms

from AutoJaliApp.models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model =Order
        fields = '__all__'
