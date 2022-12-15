from django import forms

from .models import Post, Tag


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = (
            Post.name.field.name,
            Post.image.field.name,
            Post.text.field.name,
            Post.category.field.name,
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
