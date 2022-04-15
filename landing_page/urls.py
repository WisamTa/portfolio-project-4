from django.urls import path
from .views import Index
from socialnetwork import urls

urlpatterns = [
    path('', Index.as_view(), name='index'),
]