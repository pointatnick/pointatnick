from django.http import HttpResponse

def home(request):
   return HttpResponse("Hello world, you are the home page.")
