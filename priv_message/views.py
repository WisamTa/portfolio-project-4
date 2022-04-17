from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.db.models import Q
from .models import Inbox, Thread
from .forms import InboxForm, MessageForm


class InboxList(View):
    """
    Class to get all the threads in the inbox
    """
    def get(self, request, *args, **kwargs):
        inboxthread = Inbox.objects.filter(
            Q(user=request.user) | Q(user_receiver=request.user))

        context = {
            'inboxthread': inboxthread,
            
        }
        return render(request, 'private_message.html', context)


class CreateInboxForm(View):
    """
    Class for search a user to start a chat with
    """
    def get(self, request, *args, **kwargs):
        form = InboxForm()

        context = {
            'form': form
        }

        return render(request, 'message_search.html', context)

    def post(self, request, *args, **kwargs):
        form = InboxForm(request.POST)

        username = request.POST.get('username')
        print(username)

        try:
            user_receiver = User.objects.get(username=username)
            if Inbox.objects.filter(user=request.user, user_receiver=user_receiver).exists():
                inbox_thread = Inbox.objects.filter(user=request.user, user_receiver=user_receiver)[0]

                return redirect('message', pk=inbox_thread.pk)
                       
            elif Inbox.objects.filter(user=user_receiver, user_receiver=request.user).exists():
                inbox_thread = Inbox.objects.filter(user=user_receiver, user_receiver=request.user)[0]

                return redirect('message', pk=inbox_thread.pk)

            if form.is_valid():
                inbox_thread = Inbox(user=request.user, user_receiver=user_receiver)
                inbox_thread.save()

                return redirect('message', pk=inbox_thread.pk)
        except:
            return redirect('new-thread')


class Message(View):
    """
    Class for the form to create a message in the specific chat to the user and hold
    the information
    """
    def get(self, request, pk, *args, **kwargs):
        send_form = MessageForm()
        inbox_thread = Inbox.objects.get(pk=pk)
        print(inbox_thread)
        message_thread = Thread.objects.filter(thread__pk__contains=pk)
        print(message_thread)

        context = {
            'inbox_thread': inbox_thread,
            'send_form': send_form,
            'message_thread': message_thread
        }
        return render(request, 'direct_message.html', context)


class CreateMessage(View):
    """
    Class for POST the message to the user and hold the send form 
    """
    def post(self, request, pk, *args, **kwargs):
        inbox_thread = Inbox.objects.get(pk=pk)
        if inbox_thread.user_receiver == request.user:
            user_receiver = inbox_thread.user
        else:
            user_receiver = inbox_thread.user_receiver
        
        message = Thread(
            thread=inbox_thread,
            sender=request.user,
            receiver=user_receiver,
            body=request.POST.get('message')
        )
        message.save()

        return redirect('message', pk=pk)