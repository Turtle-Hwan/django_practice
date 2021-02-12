from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return render(request, 'name.html')

def mainPage(request):
    return render(request, 'mainPage.html')