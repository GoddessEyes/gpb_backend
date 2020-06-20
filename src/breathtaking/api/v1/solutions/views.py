from breathtaking.api.common.viewsets import CreateDestroyViewSet
from breathtaking.api.v1.solutions.serializers import (
    SolutionWithIdeaSerializer,
    SolutionWithoutIdeaSerializer,
)
from breathtaking.modules.solutions.models import Solution


class SolutionWithoutIdeaViewSet(CreateDestroyViewSet):
    """Бизнес решение без привязки к идее.
    Тэги выбираются самостоятельно.
    """
    serializer_class = SolutionWithoutIdeaSerializer
    queryset = Solution.objects.all()


class SolutionWithIdeaViewSet(CreateDestroyViewSet):
    """Бизнес решение с привязкой к идее.
    Тэги выбираются автоматически из идеи.
    """
    serializer_class = SolutionWithIdeaSerializer
    queryset = Solution.objects.all()
