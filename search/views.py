from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import Q
from django.views import View
from socialnetwork.models import Users
from django.http import JsonResponse


class Search(ListView):
    def get(self, request, *args, **kwargs):
        return render(request, 'search_users.html')


def get_result(request):
    if request.is_ajax():

        result = None
        username = request.POST.get('username')
        query = Users.objects.filter(user__username__icontains=username)

        if len(query) > 0 and len(username) > 0:
            data = []
            for i in query:
                item = {
                    'pk': i.pk,
                    'user': i.user.username,
                }
                data.append(item)
            result = data
            print(data)
        else:
            result = 'Sorry, no one with that username could be find!'

        return JsonResponse({
            'success': '',
            'data': result
            })
    return JsonResponse({})
