from . import views
from django.urls import path

urlpatterns = [
    path('', views.dashboard_content, name='dashboard'),
]