import requests

URL_BASE = "https://mon-site/api/cible"
AUTH = ("utilisateur", "mot de passe")
HEADERS = {"Content-type": "application/json"}

url_get = URL_BASE + "/get/users/"
url_post = URL_BASE + "/post/users/"

response = requests.get(url_get, auth=AUTH, headers=HEADERS)
response = requests.post(url_post, auth=AUTH, headers=HEADERS)

if response.status_code == 200:
    print("requête  OK")
    print(response.json())
else:
    print("à toi de voir")

# https://community.infoblox.com/