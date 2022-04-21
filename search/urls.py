from django.urls import path
from .views import Search, get_result
from socialnetwork.views import UserProfile


urlpatterns = [
    path('search/', Search.as_view(), name='search_user'),
    path('result/', get_result, name='result-list'),
    path('search/<pk>/', UserProfile.as_view(), name='search_user'),
]
