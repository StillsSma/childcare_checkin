from django import forms

class PinForm(forms.Form):
    pin = forms.CharField(max_length=4)
