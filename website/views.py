from django.shortcuts import render


def home(request):
    return render(request, 'website/home.html')


def archive(request):
    return render(request, 'website/archive.html')


def projects(request):
    return render(request, 'website/projects.html')


def about(request):
    return render(request, 'website/about.html')
