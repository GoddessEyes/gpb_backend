from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.viewsets import ReadOnlyModelViewSet

from breathtaking.api.common.viewsets import ListCreateDestroyViewSet
from breathtaking.api.v1.solutions.serializers import (
    SolutionSerializer,
    SolutionWithIdeaSerializer,
    SolutionWithoutIdeaSerializer,
)
from breathtaking.modules.solutions.models import Solution


class SolutionWithoutIdeaViewSet(ListCreateDestroyViewSet):
    """Бизнес решение без привязки к идее.
    Тэги выбираются самостоятельно.
    """
    serializer_class = SolutionWithoutIdeaSerializer
    queryset = Solution.objects.all()


class SolutionWithIdeaViewSet(ListCreateDestroyViewSet):
    """Бизнес решение с привязкой к идее.
    Тэги выбираются автоматически из идеи.
    """
    serializer_class = SolutionWithIdeaSerializer
    queryset = Solution.objects.all()


class SolutionViewSet(ReadOnlyModelViewSet):
    """Все Бизнес решения."""
    serializer_class = SolutionSerializer
    queryset = Solution.objects.all()

    filter_backends = (
        SearchFilter,
        DjangoFilterBackend,
        OrderingFilter,
    )

    search_fields = (
        'short_description',
        'task',
        'description',
        'result',
        'resources',
    )
    filter_fields = (
        'user',
        'idea',
        'tags',
        'themes',
    )

    ordering_fields = (
        'created',
        'modified',
    )
