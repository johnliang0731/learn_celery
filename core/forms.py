# core/forms.py
from django import forms

class SendEmailForm(forms.Form):
    email = forms.EmailField()
    content = forms.CharField()