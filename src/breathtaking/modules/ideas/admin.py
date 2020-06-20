"""Модуль django-admin `Идей`."""

from django.contrib import admin

from breathtaking.modules.ideas.models import IdeaComment, IdeaLike, IdeaOffer, Tag, Theme


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
    )
    list_editable = (
        'status',
    )
    list_display = (
        'theme',
        'user',
        'status',
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
