from django.urls import path
from .views import InboxList, CreateInboxForm

urlpatterns = [
    path('inbox/', InboxList.as_view(), name='inbox'),
    path('inbox/start-chat', InboxList.as_view(), name='priv-message'),
]