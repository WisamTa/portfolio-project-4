from django.shortcuts import render
from django.db.models import Q
from django.views import View
from socialnetwork.models import Users


class Search(View):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('query', None)
        if not query:
            query = ""

        results = Users.objects.filter(
            Q(user__username__icontains=query)
        )

        return render(request, 'search_users.html', {'results': results})
