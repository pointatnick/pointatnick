from django.http import HttpResponse

def home(request):
   return HttpResponse("the home page")


def about(request):
    return HttpResponse("the about page")


def projects(request):
    return HttpResponse("the projects page")
