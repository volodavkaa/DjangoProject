from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    return render(request, "home.html")

def contact(request):
    return render(request, "contact.html")
