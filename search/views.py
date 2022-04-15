from django.shortcuts import render
from django.views import View
from socialnetwork import views


class Search(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'search_users.html')
