from django.shortcuts import render

def home(request):
   return render(request, 'home/welcome.html')

def authorized(request):
    return render(request, 'home/authorized.html')