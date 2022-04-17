from django.urls import path
from .views import PostList, Upload, PostDetail, PostEdit, PostDelete, CommentDelete, UserProfile, UserProfileEdit, PostLike


urlpatterns = [
    path('', PostList.as_view(), name='post_feed'),
    path('post/upload', Upload.as_view(), name='upload'),
    path('post/<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('post/<int:pk>/like', PostLike.as_view(), name='post_like'),
    path('post/edit/<int:pk>', PostEdit.as_view(), name='post_edit'),
    path('post/delete/<int:pk>', PostDelete.as_view(), name='post_delete'),
    path('post/<int:post_pk>/comment/delete<int:pk>', CommentDelete.as_view(), name='comment_delete'),
    path('profile/<int:pk>', UserProfile.as_view(), name='profile'),
    path('profile/edit/<int:pk>', UserProfileEdit.as_view(), name='profile_edit'),
]