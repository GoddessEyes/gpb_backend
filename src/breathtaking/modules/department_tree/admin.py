"""Модуль django-admin."""

from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from breathtaking.modules.department_tree.models import DepartmentTree


@admin.register(DepartmentTree)
class DepartmentTreeAdmin(DraggableMPTTAdmin):
    """Регистрация MPTT модели в админ-панеле."""
