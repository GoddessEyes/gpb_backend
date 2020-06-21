from breathtaking.api.common.viewsets import ListOnlyModelViewSet
from breathtaking.api.v1.userprofile.serializers import UserInfoSerializer
from breathtaking.modules.eauth.models import User


class UserProfileViewSet(ListOnlyModelViewSet):
    serializer_class = UserInfoSerializer
    queryset = User.objects.all()

    def get_queryset(self):
        return self.queryset.filter(
            id=self.request.user.id,
        )
