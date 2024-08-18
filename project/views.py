from django.shortcuts import render
from django.views import View
from .models import project_detail
from .forms import EmojiSelection

# Create your views here.

class ProjectView(View):
    def get(self, request):
        approved_projects = project_detail.objects.filter(approved=True)

        return render(
            request, 
            "project/project.html",
            {'projects':approved_projects}
        )


def dashboard_content(request):

    projects = project_detail.objects.all().order_by("-favourite")

    search = request.GET.get("project-search")
    search_results = project_detail.objects.filter(title__icontains=search).values() if search != None else ''

    if request == 'POST':
        emoji_form = EmojiSelection(data=request.POST)
        if emoji_form.is_valid():
            emoji = emoji_form.save(commit=False)
            emoji.account = request.user
            emoji.save()
    
    emoji_form = EmojiSelection()

    return render(
        request,
        'project/dashboard.html',
        {
            'projects' : projects,
            'search_results' : search_results,
            'emoji_form' : emoji_form,
        },
    )
