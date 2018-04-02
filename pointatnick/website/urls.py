from django.urls import path

from . import views


app_name = 'website'
urlpatterns = [
    path('', views.home, name='home'),
    path('archive', views.archive, name='archive'),
    path('projects', views.projects, name='projects'),
    path('resume', views.resume, name='resume'),
    path('about', views.about, name='about')
]
