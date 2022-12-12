from core.models import NamedBaseModel, PublishableBaseModel, SluggedBaseModel
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.safestring import mark_safe
from sorl.thumbnail import get_thumbnail

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

    objects = ItemManager()

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'
        default_related_name = 'items'

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
