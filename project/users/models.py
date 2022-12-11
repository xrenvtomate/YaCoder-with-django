from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin,
                                        UserManager)
from django.db import models
from django.urls import reverse


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        'имя пользователя',
        max_length=150,
        help_text='Не более 150 символов',
    )
    email = models.EmailField(
        'электронная почта',
        max_length=254,
        unique=True,
        help_text='Не более 254 символов',
    )

    first_name = models.CharField(
        'имя',
        max_length=254,
        blank=True,
        null=True,
        help_text='Не более 254 символов',
    )
    last_name = models.CharField(
        'фамилия',
        max_length=254,
        blank=True,
        null=True,
        help_text='Не более 254 символов',
    )
    about_me = models.TextField(
        'описание',
        default='Sample Text',
        help_text='Обо мне',
        blank=True,
    )

    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        default_related_name = 'users'

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:user_detail', kwargs={"pk": self.pk})
