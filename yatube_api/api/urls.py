from django.urls import include, path

from rest_framework import routers

from api.views import (
    PostViewSet,
    GroupViewSet,
    CommentViewSet,
    FollowingViewSet
)


router = routers.SimpleRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'groups', GroupViewSet, basename='group')
router.register(r'posts/(?P<post_id>\d+)/comments',
                CommentViewSet,
                basename='comments')
router.register(r'follow', FollowingViewSet, basename='follow')


urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
