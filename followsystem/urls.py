from django.urls import path
from .views import AddFollower, UnFollow

urlpatterns = [
    path('profile/<int:pk>/followers/add',
         AddFollower.as_view(), name='add_follower'),
    path('profile/<int:pk>/followers/remove',
         UnFollow.as_view(), name='un_follow'),
]
