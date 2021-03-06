"""Роуты для API приложения. Схема API."""

from typing import Tuple

from django.urls import URLResolver, include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from breathtaking.api.v1.ideas.urls import router as ideas_router
from breathtaking.api.v1.solutions.urls import router as solutions_router
from breathtaking.api.v1.stats.urls import router as stats_router
from breathtaking.api.v1.userprofile.urls import router as userprofile_router


schema_view = get_schema_view(
    openapi.Info(
        title='Breathtaking API',
        default_version='v1',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns: Tuple[URLResolver, ...] = (
    path('ideas/', include(ideas_router.urls)),
    path('solution/', include(solutions_router.urls)),
    path('statistic/', include(stats_router.urls)),
    path('userprofile/', include(userprofile_router.urls)),
    path('auth/', include('breathtaking.api.v1.auth.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
)
