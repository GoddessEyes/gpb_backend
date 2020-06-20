"""Модуль сериализации объектов `Идей` и их связей."""

from rest_framework import serializers

from breathtaking.api.v1.auth.serializers import UserSerializer
from breathtaking.api.v1.solutions.serializers import SolutionSerializer
from breathtaking.modules.ideas.models import IdeaComment, IdeaLike, IdeaOffer, Tag, Theme


class IdeaCommentSerializer(serializers.ModelSerializer):
    """Сериалайзер комментариев к идеи."""

    class Meta:
        model = IdeaComment
        exclude = (
            'user',
        )

    def create(self, validated_data):
        idea_comment, _ = IdeaComment.objects.get_or_create(
            user=self.context['request'].user,
            idea=validated_data['idea'],
            comment=validated_data['comment'],
        )
        return idea_comment


class IdeaLikeSerializer(serializers.ModelSerializer):
    """Сериалайзер лайков к идеи."""

    class Meta:
        model = IdeaLike
        exclude = (
            'user',
        )

    def create(self, validated_data):
        idea_like, _ = IdeaLike.objects.get_or_create(
            user=self.context['request'].user,
            idea=validated_data['idea'],
        )
        return idea_like


class TagSerializer(serializers.ModelSerializer):
    """Сериалайзер тэгов идеи."""

    class Meta:
        model = Tag
        fields = '__all__'


class ThemeSerializer(serializers.ModelSerializer):
    """Сериалайзер тем идей."""

    class Meta:
        model = Theme
        fields = '__all__'
        read_only_fields = (
            'id',
            'name',
        )


class IdeaOfferSerializer(serializers.ModelSerializer):
    """Сериалайзер `идей`."""
    user = serializers.SerializerMethodField(read_only=True)
    like_count = serializers.SerializerMethodField()
    comment_count = serializers.SerializerMethodField()
    idealike_set = IdeaLikeSerializer(
        many=True,
        read_only=True,
        help_text='Массив лайков'
    )
    themes_info = serializers.SerializerMethodField(read_only=True)
    tags_info = serializers.SerializerMethodField(read_only=True)
    ideacomment_set = IdeaLikeSerializer(many=True, read_only=True)
    status = serializers.IntegerField(read_only=True)
    solution_set = SolutionSerializer(read_only=True, many=True)

    class Meta:
        model = IdeaOffer
        fields = '__all__'

    def get_themes_info(self, instance):
        return ThemeSerializer(instance.themes).data

    def get_tags_info(self, instance):
        return TagSerializer(instance.tags, many=True).data

    def get_like_count(self, instance):
        """Вернёт в сериалзиацию кол-во лайков идеи."""
        return instance.idealike_set.count()

    def get_comment_count(self, instance):
        """Вернёт в сериалзиацию кол-во комментов идеи."""
        return instance.ideacomment_set.count()

    def get_user(self, instance):
        return UserSerializer(instance.user).data

    def create(self, validated_data):
        idea_offer = IdeaOffer.objects.create(
            user=self.context['request'].user,
            theme=validated_data['theme'],
            description=validated_data['description'],
            themes=validated_data['themes'],
        )
        idea_offer.tags.set(validated_data['tags'])
        return idea_offer
