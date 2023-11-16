from django.shortcuts import render
import os
import requests
from dotenv import load_dotenv

load_dotenv()

def proyectos(request):
    url = 'https://api.github.com/users/wilovy09/repos'
    headers = {
        'Authorization': f'Bearer {os.getenv("GITHUB_TOKEN")}',
        'Accept': 'application/vnd.github.v3+json'
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        repos = []
        
        for repo in data:
            repo_data = {
                'name': repo['name'],
                'description': repo['description'],
                'html_url': repo['html_url'],
                'homepage': repo['homepage'],
                'language': repo['language'],
                'owner_login': repo['owner']['login'],
                'owner_avatar_url': repo['owner']['avatar_url']
            }
            repos.append(repo_data)

        return render(request, 'proyectos.html', {'repos': repos})
    else:
        print("Ha ocurrido un error:", response.status_code)
