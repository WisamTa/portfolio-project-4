from django import forms
from .models import Inbox, Thread


class InboxForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        label='',
        widget=forms.Textarea(attrs={
            'rows': '1',
            'placeholder': 'Username'
        })
    )


class MessageForm(forms.Form):
    message = forms.CharField(
        label='',
        max_length=500,
        widget=forms.Textarea(attrs={
            'rows': '3',
            'placeholder': 'Write a message here...'
        })
    )
