rom django import forms
from django.forms import ModelForm
from .models import Post, Comment


class PostForm(forms.ModelForm):
    body = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '2',
            'placeholder': 'Whats on your mind today?...'
        })
    )

    upload = forms.ImageField(required=False)

    class Meta:
        model = Post
        fields = ['body', 'upload']


class CommentForm(forms.ModelForm):
    comment = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '2',
            'placeholder': 'Leave a comment...'
        })
    )

    class Meta:
        model = Comment
        fields = ['comment']