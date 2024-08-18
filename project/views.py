from django.shortcuts import render
from django.views import View
from .models import project_detail

# Create your views here.
class ProjectView(View):
    def get(self, request):
        return render(request, "project/project.html")

def dashboard_content(request):

    projects = project_detail.objects.all()

    return render(
        request,
        'project/dashboard.html',
        {'projects' : projects},
    )
