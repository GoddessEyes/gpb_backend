from rest_framework import serializers

from breathtaking.modules.ideas.models import IdeaComment, IdeaLike, IdeaOffer, Tag, Theme


class IdeaCommentSerializer(serializers.ModelSerializer):
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
    class Meta:
        model = Tag
        fields = '__all__'


class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = '__all__'


class IdeaOfferSerializer(serializers.ModelSerializer):
    like_count = serializers.SerializerMethodField()
    comment_count = serializers.SerializerMethodField()

    idealike_set = IdeaLikeSerializer(
        many=True,
        read_only=True,
        help_text='Массив лай'
    )
    ideacomment_set = IdeaLikeSerializer(many=True, read_only=True)
    status = serializers.IntegerField(read_only=True)

    class Meta:
        model = IdeaOffer
        exclude = (
            'user',
        )

    def get_like_count(self, instance):
        return instance.idealike_set.count()

    def get_comment_count(self, instance):
        return instance.ideacomment_set.count()

    def create(self, validated_data):
        idea_offer = IdeaOffer.objects.create(
            user=self.context['request'].user,
            theme=validated_data['theme'],
            description=validated_data['description'],
        )
        idea_offer.tags.set(validated_data['tags'])
        idea_offer.themes.set(validated_data['themes'])
        return idea_offer
