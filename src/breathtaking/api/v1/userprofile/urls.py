"""Модуль роутинга эндопинтов `solutions`."""

from rest_framework import routers

from breathtaking.api.v1.userprofile.views import UserProfileViewSet


router = routers.DefaultRouter()

router.register('userprofile', UserProfileViewSet)
