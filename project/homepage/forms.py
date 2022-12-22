from django import forms

from .models import Comment, Post, Tag


class CommentForm(forms.ModelForm):
    editing = forms.IntegerField(
        required=False,
        disabled=True,
        widget=forms.HiddenInput(),
        )

    class Meta:
        model = Comment
        fields = (
            Comment.text.field.name,
            Comment.parent_comment.field.name,
            Comment.replied_comment.field.name,
            'editing',

        )
        labels = {
            Comment.text.field.name: 'Write your comment',
        }
        widgets = {
            Comment.parent_comment.field.name: forms.HiddenInput(),
            Comment.replied_comment.field.name: forms.HiddenInput(),
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
