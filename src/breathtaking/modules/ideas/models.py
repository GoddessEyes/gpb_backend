from django.conf import settings
from django.db import models


class Theme(models.Model):
    name = models.CharField(
        verbose_name='Тема',
        max_length=255,
    )


class Tag(models.Model):
    name = models.CharField(
        verbose_name='Тэг',
        max_length=255,
    )


class IdeaOffer(models.Model):
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
    themes = models.ManyToManyField(
        to=Theme,
        verbose_name='Темы',
    )
    status = models.PositiveSmallIntegerField(
        verbose_name='Статус',
        choices=(
            (0, 'Опубликовано'),
            (1, 'Модерация'),
            (2, 'Не прошло модерацию'),
        ),
        default=1,
    )

    class Meta:
        verbose_name = 'Идея'
        verbose_name_plural = 'Идеи'

    def __str__(self):
        return f'{self.theme} {self.user}'


class IdeaLike(models.Model):
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


class IdeaComment(models.Model):
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
