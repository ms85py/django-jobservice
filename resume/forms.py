

from django import forms


class NewForm(forms.Form):
    description = forms.CharField(max_length=1024)