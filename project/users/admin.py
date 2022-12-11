from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User


class ProfileInlined(admin.StackedInline):
    model = User


class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInlined,)


admin.site.register(User)
