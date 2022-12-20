from django.db import models
from django.db.models.functions import Coalesce

from . import models as local_models


class PostManager(models.Manager):
    def published_main(self):
        return (
            self.get_queryset()
                .filter(
                    is_published=True,
                    )
                .select_related('prog_language')
                .order_by('name')
                .prefetch_related(
                    models.Prefetch(
                        'tags',
                        queryset=local_models.Tag.objects.all()
                    )
                )
        )


class CommentManager(models.Manager):
    def select_by_new(self):
        return (
            self.get_queryset()
                .order_by(
                    Coalesce(
                        'parent_comment',
                        'pk',
                    )
                )
        )
