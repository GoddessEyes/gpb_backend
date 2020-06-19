from django.db import models


class TimeStampedModel(models.Model):
    """Абстрактная модель с полями created и modified."""

    created = models.DateTimeField(
        'Создано',
        auto_now_add=True,
        null=True,
    )
    modified = models.DateTimeField('Изменено', auto_now=True, null=True,)

    class Meta:
        abstract = True
