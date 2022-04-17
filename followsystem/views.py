from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views import View
from django.http import HttpResponseRedirect
from socialnetwork.models import Users


class AddFollower(LoginRequiredMixin, View):
    """
    Class view for adding a user and start follow them 
    """
    def post(self, request, pk, *args, **kwargs):
        profile = Users.objects.get(pk=pk)
        profile.followers.add(request.user)

        return redirect('profile', pk=profile.pk)


class UnFollow(LoginRequiredMixin, View):
    """
    Class View for unfaollow a user that you already follow 
    """
    def post(self, request, pk, *args, **kwargs):
        profile = Users.objects.get(pk=pk)
        profile.followers.remove(request.user)

        return redirect('profile', pk=profile.pk)
