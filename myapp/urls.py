from django.urls import path  # For Django routing
from . import views  # Assuming your views are in the same app
from django.conf import settings
from django.conf.urls.static import static
from pathlib import Path
from .views import contact_view

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('contact/', contact_view, name='contact'),
]
