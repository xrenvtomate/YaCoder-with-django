from django.db import models

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

    def published_by_category(self):
        return (
            self.get_queryset()
                .filter(is_published=True)
                .select_related('category')
                .order_by(
                    'category__name',
                    'name'
                    )
                .prefetch_related(
                    models.Prefetch(
                        'tags',
                        queryset=local_models.Tag.objects.all()
                    )
                )
        )
