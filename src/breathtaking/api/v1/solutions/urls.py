"""Модуль роутинга эндопинтов `solutions`."""

from rest_framework import routers

from breathtaking.api.v1.solutions.views import (
    SolutionViewSet,
    SolutionWithIdeaViewSet,
    SolutionWithoutIdeaViewSet,
)


router = routers.DefaultRouter()

router.register('solutions_without_idea', SolutionWithoutIdeaViewSet)
router.register('solutions_with_idea', SolutionWithIdeaViewSet)
router.register('solutions_all', SolutionViewSet)
