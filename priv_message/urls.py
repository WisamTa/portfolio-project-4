from django.urls import path
from .views import InboxList, DeleteInboxThread, CreateInboxForm, Message
from .views import CreateMessage

urlpatterns = [
    path('chats/', InboxList.as_view(), name='inbox'),
    path('chats/delete/<int:pk>', DeleteInboxThread.as_view(),
         name='delete-thread'),
    path('chats/new-thread/', CreateInboxForm.as_view(), name='new-thread'),
    path('chats/<int:pk>/', Message.as_view(), name='message'),
    path('chats/<int:pk>/send/', CreateMessage.as_view(), name='send'),

]
