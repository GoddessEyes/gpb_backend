from rest_framework import serializers


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
        return 3
