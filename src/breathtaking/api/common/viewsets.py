"""Кастомные Viewsets."""

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet


class CreateDestroyViewSet(mixins.CreateModelMixin, mixins.DestroyModelMixin, GenericViewSet):
    """Предоставляет дефолтные методы: `create()`, `destroy()`."""


class ListCreateDestroyViewSet(
    mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, GenericViewSet
):
    """Предоставляет дефолтные методы: `create()`, `destroy()`."""


class ListOnlyModelViewSet(mixins.ListModelMixin, GenericViewSet):
    """Предоставляет дефолтный метод: `list()`."""


class RetrieveOnlyModelViewSet(mixins.RetrieveModelMixin):
    """Предоставляет дефолтный метод: `retrieve()`."""
