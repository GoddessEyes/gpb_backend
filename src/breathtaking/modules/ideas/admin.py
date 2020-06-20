"""Модуль django-admin `Идей`."""

from django.contrib import admin

from breathtaking.modules.ideas.models import IdeaComment, IdeaLike, IdeaOffer, Tag, Theme
from breathtaking.modules.solutions.models import Solution


class SolutionInline(admin.TabularInline):
    """Инлайн админ `Решения к идее`."""

    model = Solution
    extra = 0


class IdeaLikeInline(admin.TabularInline):
    """Инлайн админ `Лайки к идее`."""

    model = IdeaLike
    extra = 0


class IdeaCommentInline(admin.TabularInline):
    """Инлайн админ `Комменты к идее`."""

    model = IdeaComment
    extra = 0


@admin.register(IdeaOffer)
class IdeaOfferAdmin(admin.ModelAdmin):
    """Админ класс идеи для админ-панели."""

    inlines = (
        IdeaLikeInline,
        IdeaCommentInline,
        SolutionInline,
    )
    list_editable = (
        'status',
    )
    list_display = (
        'theme',
        'user',
        'status',
        'themes',
    )
    readonly_fields = (
        'created',
        'modified',
    )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """Тэги идей."""


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    """Темы идей."""
