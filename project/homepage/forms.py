from django import forms

from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = (
            Post.name.field.name,
            Post.image.field.name,
            Post.text.field.name,
            Post.category.field.name,
            Post.tags.field.name,
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
