from django.shortcuts import render
from django.views import View
from .models import project_detail

# Create your views here.
class ProjectView(View):
    def get(self, request):
        return render(request, "project/project.html")

def dashboard_content(request):

    projects = project_detail.objects.all().order_by("-favourite")

    search = request.GET.get("project-search")
    search_results = project_detail.objects.filter(title__icontains=search).values() if search != None else ''

    return render(
        request,
        'project/dashboard.html',
        {
            'projects' : projects,
            'search_results' : search_results,
        },
    )
