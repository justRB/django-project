from django.shortcuts import render
from django.views import View

# SHOW
class AppHome(View):
    def get(selft, request):
        return render(request, template_name="app/home.html")