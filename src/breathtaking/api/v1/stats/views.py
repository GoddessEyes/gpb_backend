from rest_framework.response import Response

from breathtaking.api.common.viewsets import ListOnlyModelViewSet
from breathtaking.api.v1.stats.serializers import MainHeaderStats, StatsSerializer
from breathtaking.modules.eauth.models import User
from breathtaking.modules.ideas.models import IdeaOffer


class StatisticViewSet(ListOnlyModelViewSet):
    serializer_class = StatsSerializer
    queryset = User.objects.all()

    def get_queryset(self):
        return self.queryset.filter(
            id=self.request.user.id,
        )


class MainHeaderStatisticViewSet(ListOnlyModelViewSet):
    serializer_class = MainHeaderStats
    queryset = IdeaOffer.objects.all()

    def list(self, request, *args, **kwargs):
        serializer = MainHeaderStats(self.queryset)
        return Response(serializer.data)
