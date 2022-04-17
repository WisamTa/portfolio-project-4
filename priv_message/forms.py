from django import forms
from .models import Inbox

class InboxForm(forms.Form):
    username = forms.CharField(max_length=100, label='')