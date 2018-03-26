from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'website/home.html')


def about(request):
    return HttpResponse("the about page")


def projects(request):
    return HttpResponse("the projects page")
