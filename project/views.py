from django.shortcuts import render
from .models import project_detail

# Create your views here.
def dashboard_content(request):
    
    return render(
        request,
        'project/dashboard.html',
    )

