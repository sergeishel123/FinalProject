from django import forms
from django_summernote.fields import SummernoteTextField,SummernoteWidget
from .models import Post,Category


class PostForm(forms.ModelForm):
    category = forms.CharField(max_length = 64)
    text = SummernoteWidget()
    class Meta:
        model = Post
        fields = (
            'heading',
            'text'
        )

