
from breathtaking.api.common.viewsets import ListCreateDestroyViewSet
from breathtaking.api.v1.solutions.serializers import (
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
