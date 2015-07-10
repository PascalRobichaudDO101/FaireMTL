import requests

#import bs4
from bs4 import BeautifulSoup

r = requests.get('https://fairemtl.ca/fr/affichage-dynamique-vers-stationnement-disponible')

if (r.status_code == requests.codes.ok):

  #print(r.url)
  #print(r.headers)
  #print(r.content)
  #print(r.text)

  la_page = r.text.encode('ascii', 'ignore')
  #print(value)
  #value = unicode(r.text, "utf-8")
  
  #print(r.encoding)
  #r.encoding = 'ISO-8859-1'
  #print(r.encoding)
  soup = bs4.BeautifulSoup(la_page)
  #soup = BeautifulSoup(la_page, 'html.parser')
  print(soup)
  
  print('Fin du traitement')
  
  
  
  
