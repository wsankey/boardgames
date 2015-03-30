from django.shortcuts import render

def home(request):
    return render(request, "person/home.html")
