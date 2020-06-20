from breathtaking.api.common.viewsets import ListOnlyModelViewSet
from breathtaking.api.v1.stats.serializers import StatsSerializer
from breathtaking.modules.eauth.models import User


class StatisticViewSet(ListOnlyModelViewSet):
    serializer_class = StatsSerializer
    queryset = User.objects.all()

    def get_queryset(self):
        return self.queryset.filter(
            id=self.request.user.id,
        )
