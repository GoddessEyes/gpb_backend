from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class DepartmentTree(MPTTModel):
    name = models.CharField(
        verbose_name='Название отдела',
        max_length=255,
    )
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children',
        verbose_name='Родитель отдела'
    )
    users = models.ManyToManyField(
        to='eauth.User',
        verbose_name='Сотрудники',
        related_name='department_users'
    )
    department_heads = models.ManyToManyField(
        to='eauth.User',
        verbose_name='Главы отдела',
        related_name='department_heads',
    )

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'

    def __str__(self):
        return self.name
