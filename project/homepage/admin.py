from django.contrib import admin
from sorl.thumbnail.admin import AdminImageMixin

from .models import Category, Post, Tag

admin.site.register(Category)
admin.site.register(Tag)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin, AdminImageMixin):
    list_display = (
        'name',
        'text',
        'is_published',
        'image_tmb',
    )
    list_editable = (
        'is_published',
    )
    list_display_links = ('name',)
    filter_horizontal = ('tags',)
    readonly_fields = ('image_tmb',)
