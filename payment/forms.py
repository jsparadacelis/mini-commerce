from django import forms

class PayForm(forms.Form):
    num_products = forms.CharField(max_length=2, required=False)