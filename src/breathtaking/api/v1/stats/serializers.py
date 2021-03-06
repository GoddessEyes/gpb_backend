from rest_framework import serializers

from breathtaking.modules.ideas.models import IdeaOffer


class MainHeaderStats(serializers.Serializer):
    open_ideas = serializers.SerializerMethodField()
    closed_ideas = serializers.SerializerMethodField()

    def get_open_ideas(self, instance):
        return IdeaOffer.objects.filter(
            status=0
        ).count()

    def get_closed_ideas(self, instance):
        return IdeaOffer.objects.filter(
            status=3
        ).count()


class StatsSerializer(serializers.Serializer):
    """Сериализатор статистики пользователя."""

    created_idea = serializers.SerializerMethodField()
    like_count = serializers.SerializerMethodField()
    created_solutions = serializers.SerializerMethodField()
    comment_count = serializers.SerializerMethodField()
    votes = serializers.SerializerMethodField()

    def get_created_idea(self, instance):
        return instance.ideaoffer_set.count()

    def get_like_count(self, instance):
        return instance.idealike_set.count()

    def get_created_solutions(self, instance):
        return instance.solution_set.count()

    def get_comment_count(self, instance):
        return instance.ideacomment_set.count()

    def get_votes(self, instance):
        return instance.ideacomment_set.count()
