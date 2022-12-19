from core.models import NamedBaseModel, PublishableBaseModel, SluggedBaseModel
from django.db import models
from django.urls import reverse
from users.models import User
import datetime

from .managers import PostManager


class Tag(PublishableBaseModel, NamedBaseModel, SluggedBaseModel):
    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'
        default_related_name = 'tags'


class ProgLanguage(PublishableBaseModel, NamedBaseModel, SluggedBaseModel):

    class Meta:
        verbose_name = 'язык программирования'
        verbose_name_plural = 'языки программирования'
        default_related_name = 'prog_languages'


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
    created_on = models.DateTimeField(
        'дата создания',
        help_text='дата создания поста',
        auto_now_add=True,
    )
    views = models.PositiveIntegerField(
        verbose_name='просмотры',
        blank=True,
        default=0,
    )
    age_of_post = models.DurationField(
        default=datetime.timedelta(0)
    )
    popularity = models.FloatField(
        verbose_name='популярность',
        help_text='популярность поста = просмотры \ время жизни поста',
        default=0,
        blank=True,
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
        self.views += 1
        self.save()
        self.popularity = self.views / (
            datetime.datetime.now(
                tz=self.created_on.tzinfo
            ) - self.created_on
        ).total_seconds()
        return reverse('homepage:post', kwargs={"pk": self.pk})
