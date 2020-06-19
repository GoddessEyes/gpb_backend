from django.contrib import admin

from breathtaking.modules.ideas.models import IdeaComment, IdeaLike, IdeaOffer, Tag, Theme


class IdeaLikeInline(admin.TabularInline):
    model = IdeaLike
    extra = 0


class IdeaCommentInline(admin.TabularInline):
    model = IdeaComment
    extra = 0


@admin.register(IdeaOffer)
class IdeaOfferAdmin(admin.ModelAdmin):
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


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    pass
