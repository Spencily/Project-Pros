from django.contrib import admin
from django.urls import include, path
from .views import ProjectView, dashboard_content

urlpatterns = [
    path('dashboard/', dashboard_content, name='dashboard'),
    path('', ProjectView.as_view(), name='project'),
]