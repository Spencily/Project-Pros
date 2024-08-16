from django.contrib import admin
from django.urls import include, path

from .views import ProjectView

urlpatterns = [
    path('', ProjectView.as_view(), name='project'),
]