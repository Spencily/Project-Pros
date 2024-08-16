from django.shortcuts import render
from django.views import View

# Create your views here.
class ProjectView(View):
    def get(self, request):
        return render(request, "project/project.html")