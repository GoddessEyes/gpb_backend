"""Модуль роутинга эндопинтов `ideas`."""

from rest_framework import routers

from breathtaking.api.v1.ideas.views import (
    IdeaCommentViewSet,
    IdeaOfferViewSet,
    LikeIdeaViewSet,
    TagViewSet,
    ThemeViewSet,
)


router = routers.DefaultRouter()

router.register('ideas', IdeaOfferViewSet)
router.register('themes', ThemeViewSet)
router.register('tags', TagViewSet)
router.register('like', LikeIdeaViewSet)
router.register('comment', IdeaCommentViewSet)
