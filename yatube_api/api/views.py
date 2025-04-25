from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import mixins
from rest_framework import filters

from posts.models import Post, Group
from .serializers import (
    PostSerializer,
    CommentSerializer,
    GroupSerializer,
    FollowingSerializer
)
from .permissions import OwnerOrReadOnly


class ListCreateViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    pass


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (OwnerOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (OwnerOrReadOnly,)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (OwnerOrReadOnly,)

    def get_post(self):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        return post

    def get_queryset(self):
        post = self.get_post()
        new_queryset = post.comments.all()
        return new_queryset

    def perform_create(self, serializer):
        post = self.get_post()
        serializer.save(
            author=self.request.user,
            post=post
        )


class FollowingViewSet(ListCreateViewSet):
    serializer_class = FollowingSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user = self.request.user
        new_queryset = user.followings.all()
        return new_queryset
