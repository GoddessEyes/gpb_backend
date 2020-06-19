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
    """Идеи."""

    serializer_class = IdeaOfferSerializer
    queryset = IdeaOffer.objects.filter(
        status=0,
    )
    permission_classes = (IsAuthenticated, )


class ThemeViewSet(ListOnlyModelViewSet):
    """Темы."""

    serializer_class = ThemeSerializer
    queryset = Theme.objects.all()
    permission_classes = (IsAuthenticated, )


class TagViewSet(ListOnlyModelViewSet):
    """Тэги."""

    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    permission_classes = (IsAuthenticated, )


class LikeIdeaViewSet(CreateDestroyViewSet):
    """Лайк к идее."""

    serializer_class = IdeaLikeSerializer
    queryset = IdeaLike.objects.all()
    permission_classes = (IsAuthenticated,)


class IdeaCommentViewSet(CreateDestroyViewSet):
    """Коммент к идее."""

    serializer_class = IdeaCommentSerializer
    queryset = IdeaComment.objects.all()
    permission_classes = (IsAuthenticated,)
