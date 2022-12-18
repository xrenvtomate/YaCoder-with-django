from core.models import NamedBaseModel, PublishableBaseModel, SluggedBaseModel
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse
from users.models import User

from .managers import PostManager


class Tag(PublishableBaseModel, NamedBaseModel, SluggedBaseModel):
    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'
        default_related_name = 'tags'


class ProgLanguage(PublishableBaseModel, NamedBaseModel, SluggedBaseModel):
    weight = models.IntegerField(
        default=100,
        help_text='Вес категории',
        validators=(
            MinValueValidator(1),
            MaxValueValidator(32766),
        ),
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        default_related_name = 'categories'


class Comment(models.Model):
    text = models.TextField(
        'комментарий',
        max_length=500,
        blank=True,
    )
    user = models.ForeignKey(
        User,
        verbose_name='пользователь',
        help_text='автор комментария',
        on_delete=models.CASCADE,
    )
    post = models.ForeignKey(
        'Post',
        verbose_name='пост',
        help_text='пост, под которым находится комментарий',
        on_delete=models.CASCADE,
    )
    prev_comment = models.ForeignKey(
        'self',
        verbose_name='комментарий сверху',
        help_text='комментарий, на который отвечает этот комментарий',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    created_on = models.DateTimeField(
        'дата создания',
        auto_now_add=True,
    )
    edited_on = models.DateTimeField(
        'дата изменения',
        blank=True,
        null=True,
        auto_now=True,
    )

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'
        default_related_name = 'comments'

    def __str__(self):
        return (f'{self.post}:{self.user}:'
                f'{self.edited_on.strftime("%Y-%m-%d %H:%M")}')


class Post(PublishableBaseModel, NamedBaseModel):
    code = models.TextField(
        'код',
        blank=True,
    )
    text = models.TextField(
        'описание',
        help_text='Описание поста',
        blank=True
    )
    prog_language = models.ForeignKey(
        ProgLanguage,
        verbose_name='язык программирования',
        help_text='ЯП',
        on_delete=models.PROTECT,
        null=True,
    )
    tags = models.ManyToManyField(
        Tag,
        verbose_name='теги',
        help_text='Теги поста'
    )
    author = models.ForeignKey(
        User,
        verbose_name='автор',
        help_text='автор комментария',
        default=1,
        on_delete=models.CASCADE,
    )

    objects = PostManager()

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'
        default_related_name = 'posts'

    def get_absolute_url(self):
        return reverse('homepage:post', kwargs={"pk": self.pk})
