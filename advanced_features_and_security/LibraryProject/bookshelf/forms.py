from django import forms


class ExampleForm(forms.Form):
    name = forms.CharField(max_length=225)
