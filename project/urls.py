from django.contrib import admin
from django.urls import include, path
from .views import ProjectView, dashboard_content, HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('dashboard/', dashboard_content, name='dashboard'),
    path('projects/', ProjectView.as_view(), name='project'),
]