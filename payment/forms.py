from django import forms

class DetailForm(forms.Form):
    name_product = forms.CharField(max_length=100)
    value_product = forms.IntegerField()
    cant_product = forms.CharField(max_length=2)