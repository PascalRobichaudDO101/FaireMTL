import requests
import BeautifulSoup

r = requests.get('https://fairemtl.ca/fr/affichage-dynamique-vers-stationnement-disponible')

if (r.status_code == requests.codes.ok):

  value = r.text.encode('ascii', 'ignore')
  #value = unicode(r.text, "utf-8")
  
  #print(r.encoding)
  #r.encoding = 'ISO-8859-1'
  #print(r.encoding)
  
  #print(r.url)
  #print(r.headers)
  #print(r.content)
  print(value)
  
  
  
  print('Fin du traitement')
  
  
  
  
