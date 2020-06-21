from rest_framework import serializers

from breathtaking.api.v1.auth.serializers import UserSerializer
from breathtaking.api.v1.stats.serializers import StatsSerializer
from breathtaking.modules.eauth.models import User
from breathtaking.modules.ideas.models import IdeaOffer
from breathtaking.modules.solutions.models import Solution


class UserProfileIdeaOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = IdeaOffer
        exclude = (
            'user',
        )


class UserProfileSolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solution
        exclude = (
            'user',
        )


class UserInfoSerializer(UserSerializer):
    """Профиль пользователя."""

    stats = serializers.SerializerMethodField()
    ideas = serializers.SerializerMethodField()
    solutions = serializers.SerializerMethodField()


    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'ideas',
            'solutions',
            'stats',
        )

    def get_ideas(self, instance):
        return UserProfileIdeaOfferSerializer(instance.ideaoffer_set.all(), many=True).data

    def get_solutions(self, instance):
        return UserProfileSolutionSerializer(instance.solution_set.all(), many=True).data

    def get_stats(self, instance):
        return StatsSerializer(instance).data
