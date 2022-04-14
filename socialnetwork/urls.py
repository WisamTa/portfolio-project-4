from django.urls import path
from .views import PostList, PostDetail, PostEdit, PostDelete, CommentDelete, UserProfile, UserProfileEdit


urlpatterns = [
    path('', PostList.as_view(), name='post_feed'),
    path('post/<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('post/edit/<int:pk>', PostEdit.as_view(), name='post_edit'),
    path('post/delete/<int:pk>', PostDelete.as_view(), name='post_delete'),
    path('post/<int:post_pk>/comment/delete<int:pk>', CommentDelete.as_view(), name='comment_delete'),
    path('profile/<int:pk>', UserProfile.as_view(), name='profile'),
    path('profile/edit/<int:pk>', UserProfileEdit.as_view(), name='profile_edit'),
]