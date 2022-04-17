from django.shortcuts import render
from django.views import View


class Index(View):
    """
    View for the landing page when user not registerd 
    """
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

class About(View):
    """
    View for render About us template in navbar
    when user not registerd 
    """
    def get(self, request, *args, **kwargs):
        return render(request, 'about_us.html')
