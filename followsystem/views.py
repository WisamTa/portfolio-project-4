from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views import View
from django.http import HttpResponseRedirect
from socialnetwork.models import Users
from socialnetwork import views



class AddFollower(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        profile = Users.objects.get(pk=pk)
        profile.followers.add(request.user)

        return redirect('profile', pk=profile.pk)


class UnFollow(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        profile = Users.objects.get(pk=pk)
        profile.followers.remove(request.user)

        return redirect('profile', pk=profile.pk)
