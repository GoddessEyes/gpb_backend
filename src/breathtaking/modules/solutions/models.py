from ckeditor.fields import RichTextField
from django.conf import settings
from django.db import models

from breathtaking.api.common.models import TimeStampedModel
from breathtaking.modules.ideas.models import IdeaOffer, Tag, Theme


class Solution(TimeStampedModel):
    """Модей бизнес решений."""

    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        verbose_name='Инициатор решения',
        on_delete=models.CASCADE,
    )
    idea = models.ForeignKey(
        to=IdeaOffer,
        verbose_name='Идея',
        on_delete=models.CASCADE,
        help_text=(
            'Если решение привязано к идее то это решение к идее. '
            'Если нет это предложение бизнес-решения.'
        ),
        blank=True,
        null=True
    )
    tags = models.ManyToManyField(
        to=Tag,
        verbose_name='Тэги',
    )
    themes = models.ForeignKey(
        to=Theme,
        verbose_name='Выбранная тема',
        on_delete=models.CASCADE,
    )
    short_description = models.CharField(
        verbose_name='Краткое описание решения',
        max_length=511,
        blank=False,
        null=False,
    )
    task = RichTextField(
        verbose_name='Задача'
    )
    description = RichTextField(
        verbose_name='Подробное описание'
    )
    result = RichTextField(
        verbose_name='Результать'
    )
    resources = RichTextField(
        verbose_name='Ресурсы'
    )
    price_min = models.DecimalField(
        verbose_name='Стоимость реализации от',
        max_length=100,
        decimal_places=2,
        max_digits=100,
    )
    price_max = models.DecimalField(
        verbose_name='Стоимость реализации до',
        max_length=100,
        decimal_places=2,
        max_digits=100,
    )

    class Meta:
        verbose_name = 'Бизнес - решение'
        verbose_name_plural = 'Бизнес - решения'

    def __str__(self):
        return f'{self.user} {self.short_description}'
