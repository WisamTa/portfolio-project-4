from django.shortcuts import render, reverse, get_object_or_404
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views import View
from .models import Followers
from .views import UserProfile
from django.http import HttpResponseRedirect


class FollowView(LoginRequiredMixin, View):

    def post(self, request, pk):
        post = get_object_or_404(UserProfile, pk=pk)

        if post.followers.filter(id=request.user.id).exists():
            post.followers.remove(request.user)
        else:
            post.followers.add(request.user)
        
        return HttpResponseRedirect(reverse('user_profile', args=[pk]))
