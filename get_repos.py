import os
import requests
from dotenv import load_dotenv
load_dotenv()
############################################################################
def get_languages(name):
    url = f'https://api.github.com/repos/wilovy09/{name}/languages'
    headers = {'X-Github-Api-Version': '2022-11-28', 'Authorization': 'Bearer ' + os.getenv('GITHUB_TOKEN'), 'Accept': 'application/vnd.github+json'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        languages_data = response.json()
        languages = list(languages_data.keys())
        print(f"Lenguajes: {', '.join(languages)}")
    else:
        print(f"Error al obtener los lenguajes del repositorio {name}. Código de estado: {response.status_code}")
############################################################################
url = 'https://api.github.com/users/wilovy09/repos'
headers = {
    'X-Github-Api-Version': '2022-11-28', 
    'Authorization': 'Bearer ' + os.getenv('GITHUB_TOKEN'),
    'Accept': 'application/vnd.github+json'
}
response = requests.get(url, headers=headers)
if response.status_code == 200:
    data = response.json()
    
    for repo in data:
        name = repo['name']
        description = repo['description']
        html_url = repo['html_url']
        homepage = repo['homepage']
        owner_login = repo['owner']['login']
        owner_avatar_url = repo['owner']['avatar_url']
        lenguajes = get_languages(name)
        # solo hay 3 vacios
        if lenguajes is None:
            lenguajes = ''
        print(lenguajes)
else:
    print("Ha ocurrido un error:", response.status_code)
############################################################################