from django import forms

from order.models import Item_in_cart


class AddToCartForm(forms.ModelForm):
    class Meta:
        model = Item_in_cart
        fields = ['quantity']
        widgets = {
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'min': '1', 'max': '10'})
        }