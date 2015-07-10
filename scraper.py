import requests

r = requests.get('https://fairemtl.ca/fr/affichage-dynamique-vers-stationnement-disponible')



print(r.content)
