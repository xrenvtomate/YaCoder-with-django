from django import forms

from .models import Post, Tag, Comment


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = (
            Comment.text.field.name,
        )
        labels = {
            Comment.text.field.name: 'Write your comment',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class PostForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all()
    )

    class Meta:
        model = Post
        fields = (
            Post.name.field.name,
            Post.prog_language.field.name,
            Post.code.field.name,
            Post.text.field.name,
            Post.tags.field.name,
        )
        labels = {
           Post.name.field.name: 'Post title',
           Post.code.field.name: 'Your code',
        }
        help_texts = {
            Post.prog_language.field.name: 'Select language',
            Post.code.field.name: 'Copy your code here',
            Post.text.field.name: 'What your code is doing?'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
