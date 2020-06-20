from rest_framework import serializers

from breathtaking.api.v1.auth.serializers import UserSerializer
from breathtaking.modules.solutions.models import Solution


class SolutionSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Solution
        fields = '__all__'

    def get_user(self, instance):
        return UserSerializer(instance.user).data


class SolutionWithoutIdeaSerializer(serializers.ModelSerializer):
    """Сериализация решений без привязки тегов и темы."""

    class Meta:
        model = Solution
        exclude = (
            'user',
            'idea',
        )

    def create(self, validated_data):
        solution = Solution.objects.create(
            user=self.context['request'].user,
            price_min=validated_data['price_min'],
            price_max=validated_data['price_max'],
            task=validated_data['task'],
            short_description=validated_data['short_description'],
            result=validated_data['result'],
            resources=validated_data['resources'],
            themes=validated_data['themes'],
            description=validated_data['description'],
        )
        solution.tags.set(validated_data['tags'])
        return solution


class SolutionWithIdeaSerializer(serializers.ModelSerializer):
    """Сериализация решений с привязкой тегов и темы."""

    class Meta:
        model = Solution
        exclude = (
            'user',
            'themes',
            'tags'
        )

    def create(self, validated_data):
        solution = Solution.objects.create(
            user=self.context['request'].user,
            price_min=validated_data['price_min'],
            price_max=validated_data['price_max'],
            idea=validated_data['idea'],
            task=validated_data['task'],
            short_description=validated_data['short_description'],
            result=validated_data['result'],
            resources=validated_data['resources'],
            themes=validated_data['idea'].themes,
            description=validated_data['description'],
        )
        solution.tags.set(validated_data['idea'].tags.all())
        return solution
