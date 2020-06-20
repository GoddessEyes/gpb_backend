"""Модуль роутинга эндопинтов `solutions`."""

from rest_framework import routers

from breathtaking.api.v1.stats.views import StatisticViewSet


router = routers.DefaultRouter()

router.register('user_stats', StatisticViewSet)
