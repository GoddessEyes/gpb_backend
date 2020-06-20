"""Модуль моделей `ideas` и её свзей."""

from django.conf import settings
from django.db import models

from breathtaking.api.common.models import TimeStampedModel


class Theme(TimeStampedModel):
    """Тема связана идеей M2M."""

    name = models.CharField(
        verbose_name='Тема',
        max_length=255,
    )

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'

    def __str__(self):
        return self.name


class Tag(TimeStampedModel):
    """Тэг связана идеей M2M."""

    name = models.CharField(
        verbose_name='Тэг',
        max_length=255,
    )

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

    def __str__(self):
        return self.name


class IdeaOffer(TimeStampedModel):
    """Заявка на идею. Создаётся в статусе проверки, публикую после модерации."""

    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        verbose_name='Инициатор идеи',
        on_delete=models.CASCADE,
    )
    theme = models.CharField(
        verbose_name='Тема идеи',
        max_length=511,
        blank=False,
        null=False,
    )
    description = models.TextField(
        verbose_name='Подробное описание идеи',
        blank=False,
        null=False,
    )
    tags = models.ManyToManyField(
        to=Tag,
        verbose_name='Тэги',
    )
    themes = models.ForeignKey(
        to=Theme,
        verbose_name='Выбранная тема',
        on_delete=models.CASCADE,
        null=True,
    )
    status = models.PositiveSmallIntegerField(
        verbose_name='Статус',
        choices=(
            (0, 'Опубликовано'),
            (1, 'Модерация'),
            (2, 'Не прошло модерацию'),
            (3, 'Решено/закрыто'),
        ),
        default=1,
    )

    class Meta:
        verbose_name = 'Идея'
        verbose_name_plural = 'Идеи'

    def __str__(self):
        return f'{self.theme} {self.user} {self.status}'


class IdeaLike(TimeStampedModel):
    """Модель лайков к идее."""

    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        verbose_name='Лайкнувший',
        on_delete=models.CASCADE,
    )
    idea = models.ForeignKey(
        to=IdeaOffer,
        verbose_name='Идея',
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'Лайк к идее'
        verbose_name_plural = 'Лайки к идее'

    def __str__(self):
        return f'{self.user} {self.idea}'


class IdeaComment(TimeStampedModel):
    """Модель комментов к идее."""

    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        verbose_name='Коментатор',
        on_delete=models.CASCADE,
    )
    idea = models.ForeignKey(
        to=IdeaOffer,
        verbose_name='Идея',
        on_delete=models.CASCADE,
    )
    comment = models.TextField(
        verbose_name='Текст комментария'
    )

    class Meta:
        verbose_name = 'Комментарий к идее'
        verbose_name_plural = 'Комментарии к идее'

    def __str__(self):
        return f'{self.user} {self.idea} {self.comment}'
