from core.models import NamedBaseModel, PublishableBaseModel, SluggedBaseModel
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe
from sorl.thumbnail import get_thumbnail
from users.models import User

from .managers import ItemManager


class Tag(PublishableBaseModel, NamedBaseModel, SluggedBaseModel):
    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'
        default_related_name = 'tags'


class Category(PublishableBaseModel, NamedBaseModel, SluggedBaseModel):
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
    image = models.ImageField(
        'изображение',
        upload_to='images/%Y/%m',
    )
    text = models.TextField(
        'описание',
        default='Sample Text',
        help_text='Описание поста',
        validators=(
        ),
        blank=True
    )
    category = models.ForeignKey(
        Category,
        verbose_name='категория',
        help_text='Категория поста',
        on_delete=models.CASCADE,
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

    objects = ItemManager()

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'
        default_related_name = 'items'

    def get_absolute_url(self):
        return reverse('homepage:post_detail', kwargs={"pk": self.pk})

    @property
    def get_img(self):
        return get_thumbnail(
            self.image,
            '300x300',
            crop='center',
            quality=50
        )

    def image_tmb(self):
        if self.image:
            return mark_safe(
                f'<img src="{self.get_img.url}"'
            )
        return 'Нет изображения'

    image_tmb.short_description = 'Изображение'
    image_tmb.allow_tags = True
