from django.contrib import admin

from breathtaking.modules.solutions.models import Solution


@admin.register(Solution)
class SolutionAdmin(admin.ModelAdmin):
    """Админ класс для бизнес решений."""

    list_display = (
        'user',
        'idea',
        'themes',
        'short_description',
        'price_min',
        'price_max',
    )
