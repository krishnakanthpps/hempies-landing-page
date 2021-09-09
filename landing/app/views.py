from django.shortcuts import render

# Create your views here.

def startView(request, *args, **kwargs):
    context = {}
    return render(request, "app/home.html")