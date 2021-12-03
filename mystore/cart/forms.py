from django import forms
from django.forms.widgets import NumberInput


class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, initial=1, widget=NumberInput(
         attrs={
            "style": "width:43px; text-align:center; border: 1px solid;"
        

        }
    ))
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)