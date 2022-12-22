from django.db import models


class PublishableBaseModel(models.Model):
    is_published = models.BooleanField(
        'is published',
        default=True
    )

    class Meta:
        abstract = True


class NamedBaseModel(models.Model):
    name = models.CharField(
        'name',
        max_length=150,
        blank=True,
    )

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return self.name
