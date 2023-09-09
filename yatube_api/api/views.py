from django.contrib.auth.models import User

from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, filters
from rest_framework.pagination import LimitOffsetPagination

from posts.models import Post, Group, Comment, Follow
from api.serializers import (
    PostSerializer,
    GroupSerializer,
    CommentSerializer,
    FollowSerializer,
)
from api.permission import OnlyAuthorHasPerm, ReadOnly


class PostViewSet(viewsets.ModelViewSet):
    '''Позволяет просматривать, создавать, редактировать и удалять посты.'''

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (OnlyAuthorHasPerm,)
    pagination_class = LimitOffsetPagination

    def get_permissions(self):
        if self.action == 'retrieve':
            return (ReadOnly(),)
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    '''Позволяет просматривать информацию о группах.'''

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    '''Чтения, создания, обновления и удаления комментариев к постам.'''

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (OnlyAuthorHasPerm,)

    def get_permissions(self):
        if self.action == 'retrieve':
            return (ReadOnly(),)
        return super().get_permissions()

    def get_post(self):
        return get_object_or_404(Post, pk=self.kwargs.get('post_id'))

    def get_queryset(self):
        return self.get_post().comments.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=self.get_post())


class FollowViewSet(viewsets.ModelViewSet):
    '''Просмотр подписок, подписка'''

    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)

    def get_following(self):
        following_username = self.request.data.get('following')
        users = get_object_or_404(User, username=following_username)
        return users

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, following=self.get_following())
