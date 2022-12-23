from django.db import models


class NamedBaseModel(models.Model):
    name = models.CharField(
        'name',
        max_length=150,
        blank=True,
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.name
