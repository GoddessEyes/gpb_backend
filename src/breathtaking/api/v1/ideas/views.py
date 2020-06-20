"""Модуль view`s для эндпоинтов `ideas`."""

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from breathtaking.api.common.viewsets import CreateDestroyViewSet, ListOnlyModelViewSet
from breathtaking.api.v1.ideas.serializers import (
    IdeaCommentSerializer,
    IdeaLikeSerializer,
    IdeaOfferSerializer,
    TagSerializer,
    ThemeSerializer,
)
from breathtaking.modules.ideas.models import IdeaComment, IdeaLike, IdeaOffer, Tag, Theme


class IdeaOfferViewSet(ModelViewSet):
    """Идеи.
    Поисковые поля: Тема и описание.
    Поля фильтраци: id-пользователя, id-тегов, id-тем, статусы =
        (0, 'Опубликовано')
        (1, 'Модерация')
        (2, 'Не прошло модерацию')
        (3, 'Решено/закрыто')
    Сортировка по: created/modified
    """

    serializer_class = IdeaOfferSerializer
    queryset = IdeaOffer.objects.all()
    permission_classes = (IsAuthenticated, )
    filter_backends = (
        SearchFilter,
        DjangoFilterBackend,
        OrderingFilter,
    )

    search_fields = (
        'theme',
        'description',
    )
    filter_fields = (
        'user',
        'tags',
        'themes',
        'status',
    )

    ordering_fields = (
        'created',
        'modified',
    )


class ThemeViewSet(ListOnlyModelViewSet):
    """"Эндпоинт `Темы`."""

    serializer_class = ThemeSerializer
    queryset = Theme.objects.all()
    permission_classes = (IsAuthenticated, )


class TagViewSet(ListOnlyModelViewSet):
    """Эндпоинт `Тэги`."""

    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    permission_classes = (IsAuthenticated, )


class LikeIdeaViewSet(CreateDestroyViewSet):
    """Эндпоинт `Лайк к идее`."""

    serializer_class = IdeaLikeSerializer
    queryset = IdeaLike.objects.all()
    permission_classes = (IsAuthenticated,)


class IdeaCommentViewSet(CreateDestroyViewSet):
    """Эндпоинт `Коммент к идее`."""

    serializer_class = IdeaCommentSerializer
    queryset = IdeaComment.objects.all()
    permission_classes = (IsAuthenticated,)
