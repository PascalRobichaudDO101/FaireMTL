import requests
import BeautifulSoup

r = requests.get('https://fairemtl.ca/fr/affichage-dynamique-vers-stationnement-disponible')

if (r.status_code == requests.codes.ok):

  print(r.url)
  #print(r.headers)
  #print(r.content)
  #print(r.text)
  
  
  
  
