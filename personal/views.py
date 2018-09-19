from django.shortcuts import render

def index(request):
    return render(request, 'personal/home.html')

def aboutme(request):
    return render(request, 'personal/aboutme.html')