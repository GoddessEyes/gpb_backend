"""Модуль моделей пользователя."""

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Переопределённая модель пользователя."""
