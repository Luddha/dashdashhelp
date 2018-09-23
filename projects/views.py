from django.shortcuts import render
import requests

def projects(request):
    user = "luddha"
    url = "https://api.github.com/users/" + user + '/repos'
    resp = requests.get(url)
    json = resp.json()

    return render(request, 'projects/projects.html', {'json': json})