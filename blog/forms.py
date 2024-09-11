# blog/forms.py

from django import forms
from .models import Comment
class CommentForm(forms.ModelForm):
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Your Name"}
        ),
    )
    email = forms.EmailField(max_length=254, widget=forms.EmailInput(attrs={
        "class": "form-control",
        "placeholder": "Your Email"
    }))
    body = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "Leave a comment!"}
        )
    )
    class Meta:
        model=Comment
        fields=['author','email','body']
        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Leave a comment!'}),

        }

        