"""Модуль django-admin."""
from allauth.account.models import EmailAddress
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from breathtaking.modules.eauth.models import User


admin.site.unregister(EmailAddress)


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """Админ-класс кастомной модели юзера."""

    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_staff',
    )

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )
