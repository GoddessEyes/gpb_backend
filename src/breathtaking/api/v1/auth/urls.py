from typing import Tuple

from django.urls import URLResolver, include, path


urlpatterns: Tuple[URLResolver, ...] = (
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
)
