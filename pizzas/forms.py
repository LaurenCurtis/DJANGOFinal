from django import forms
from .models import Pizza


class CommentForm(forms.Form):
    class Meta:
        model = Pizza
        fields = ['text']
        labels = {'text':''}