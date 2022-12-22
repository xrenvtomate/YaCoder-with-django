from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin,
                                        UserManager)
from django.db import models
from django.urls import reverse


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        'username',
        max_length=127,
        help_text='127 symbols max',
    )
    email = models.EmailField(
        'email',
        max_length=254,
        unique=True,
        help_text='254 symbols max',
    )

    first_name = models.CharField(
        'first name',
        max_length=127,
        blank=True,
        null=True,
        help_text='127 symbols max',
    )
    last_name = models.CharField(
        'last name',
        max_length=127,
        blank=True,
        null=True,
        help_text='127 symbols max',
    )
    about_me = models.TextField(
        'about me',
        default='Sample Text',
        blank=True,
    )
    profile_pic = models.ImageField(
        'profile picture',
        upload_to='images/%Y/%m',
        blank=True,
    )

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        default_related_name = 'users'

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:user_detail', kwargs={"pk": self.pk})
