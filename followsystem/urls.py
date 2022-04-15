from django.urls import path
from .views import FollowView
from socialnetwork import urls

urlpatterns = [
    path('profile/followers', FollowView.as_view(), name='followers'),
]