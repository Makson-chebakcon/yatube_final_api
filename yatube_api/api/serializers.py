import base64
from django.core.files.base import ContentFile
from django.contrib.auth import get_user_model
from rest_framework import serializers

from posts.models import Comment, Post, Group, Follow

User = get_user_model()


class Base64ImageField(serializers.ImageField):

    def to_internal_value(self, data):
        if (isinstance(data, str)
                and data.startswith("data:image")):
            format, imgstr = data.split(";base64,")
            ext = format.split("/")[-1]
            data = ContentFile(base64.b64decode(imgstr),
                               name="temp." + ext)
        return super().to_internal_value(data)


class NameRelatedField(serializers.RelatedField):

    def to_representation(self, value):
        return value.username


class PostSerializer(serializers.ModelSerializer):
    author = NameRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault()
    )
    image = Base64ImageField(required=False, allow_null=True)
    group = serializers.PrimaryKeyRelatedField(
        queryset=Group.objects.all(),
        required=False,
        allow_null=True
    )

    class Meta:
        model = Post
        fields = (
            "id",
            "text",
            "author",
            "image",
            "group",
            "pub_date",
        )


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = (
            "id",
            "title",
            "slug",
            "description",
        )


class CommentSerializer(serializers.ModelSerializer):
    author = NameRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Comment
        fields = (
            "id",
            "author",
            "post",
            "text",
            "created",
        )
        read_only_fields = ("post",)


class FollowingSerializer(serializers.ModelSerializer):
    user = NameRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault()
    )
    following = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field="username"
    )

    def validate_following(self, value):
        request_user = self.context["request"].user
        if request_user == value:
            raise serializers.ValidationError(
                "Нельзя подписываться на самого себя!"
            )
        return value

    class Meta:
        model = Follow
        fields = (
            "user",
            "following",
        )
