from django import forms

from order.models import Item_in_cart, Order


class AddToCartForm(forms.ModelForm):
    class Meta:
        model = Item_in_cart
        fields = ['quantity']
        widgets = {
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'min': '1', 'max': '10'})
        }


class OrderSubmitForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['phone_number', 'address', 'payment_method', 'comment']

    def __init__(self, *args, **kwargs):
        super(OrderSubmitForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control mb-2', })
