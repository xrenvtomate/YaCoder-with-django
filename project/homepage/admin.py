from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Comment, Post, ProgLanguage, Tag

admin.site.register(ProgLanguage)
admin.site.register(Tag)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'link_to_user',
        'link_to_post',
        'prev_comment',
        'created_on',
        'edited_on'
    )

    def link_to_user(self, obj):
        link = reverse("admin:users_user_change", args=[obj.user_id])
        return format_html('<a href="{}">{}</a>', link, obj.user.username)
    link_to_user.short_description = 'Пользователь'

    def link_to_post(self, obj):
        link = reverse("admin:homepage_post_change", args=[obj.user_id])
        return format_html('<a href="{}">{}</a>', link, obj.post.name)
    link_to_post.short_description = 'Пост'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'author',
        'code',
        'text',
        'is_published',
        'created_on',
        'views'
    )
    list_editable = (
        'is_published',
    )
    list_display_links = ('name',)
    filter_horizontal = ('tags',)
