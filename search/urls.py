from django.urls import path
from .views import Search
from socialnetwork.views import UserProfile

urlpatterns = [
    path('search/', Search.as_view(), name='search_user'),
    path('search/<int:pk>', UserProfile.as_view(), name='search_user'),
]