from core.models import NamedBaseModel, PublishableBaseModel, SluggedBaseModel
from django.db import models
from django.urls import reverse
from users.models import User

from .managers import PostManager


class Tag(PublishableBaseModel, NamedBaseModel, SluggedBaseModel):
    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'
        default_related_name = 'tags'


class ProgLanguage(PublishableBaseModel, NamedBaseModel, SluggedBaseModel):

    class Meta:
        verbose_name = 'programming language'
        verbose_name_plural = 'programming languages'
        default_related_name = 'prog_languages'


class Comment(models.Model):
    text = models.TextField(
        'comment',
        max_length=500,
        blank=True,
    )
    user = models.ForeignKey(
        User,
        verbose_name='user',
        help_text='Comment author',
        on_delete=models.CASCADE,
    )
    post = models.ForeignKey(
        'Post',
        verbose_name='post',
        help_text='Post under which the comment is written',
        on_delete=models.CASCADE,
    )
    prev_comment = models.ForeignKey(
        'self',
        verbose_name='above comment',
        help_text='Comment to which this comment is replying to',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    created_on = models.DateTimeField(
        'created on',
        auto_now_add=True,
    )
    edited_on = models.DateTimeField(
        'edited on',
        blank=True,
        null=True,
        auto_now=True,
    )

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'
        default_related_name = 'comments'

    def __str__(self):
        return (f'{self.post}:{self.user}:'
                f'{self.edited_on.strftime("%Y-%m-%d %H:%M")}')


class Post(PublishableBaseModel, NamedBaseModel):
    code = models.TextField(
        'code',
        help_text='Your code',
        blank=True,
    )
    text = models.TextField(
        'description',
        help_text='Code description',
        blank=True
    )
    prog_language = models.ForeignKey(
        ProgLanguage,
        verbose_name='programming language',
        help_text='Programming language',
        on_delete=models.PROTECT,
        null=True,
    )
    tags = models.ManyToManyField(
        Tag,
        verbose_name='tags',
        help_text='Post tags'
    )
    author = models.ForeignKey(
        User,
        verbose_name='author',
        help_text='Post author',
        default=1,
        on_delete=models.CASCADE,
    )

    objects = PostManager()

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        default_related_name = 'posts'

    def get_absolute_url(self):
        return reverse('homepage:post', kwargs={"pk": self.pk})

    def __str__(self):
        return f'{self.name}:{self.text}:'
