# -*- coding: utf-8 -*- 

#import requests
import urllib
from bs4 import BeautifulSoup
#from bs4 import NavigableString

#from bs4 import BeautifulSoup

#import urllib
#from bs4 import BeautifulSoup
#from bs4 import NavigableString
#import csv 
 #   html = urllib.urlopen(source_url)
 #   soup = BeautifulSoup(html)
 #   links = soup.findAll('a', {'title':'View opportunity'})
 #   return links

source_url = 'https://fairemtl.ca/fr/affichage-dynamique-vers-stationnement-disponible'
html = urllib.urlopen(source_url)
soup = BeautifulSoup(html)

projet = soup.find("title")
print(projet)

description = soup.find("div",{"class":"field field-name-body field-type-text-with-summary field-label-hidden"})
print(description)

onglet_commentaires = soup.find("a",{"href":"#tabs-0-footer-2"})

#Extraire le chiffre du libellé de l'onglet
for item in onglet_commentaires:
    nombre_commentaires1 = re.findall(r'[0-9]+', item.text)
    
nombre_commentaires2 = nombre_commentaires1[0]

#Afficher le nombre de commentaire (pour du débuggage)
print("Nombre de commentaires: %s" % nombre_commentaires2)	   



    
#r = requests.get(source_url)
#r = requests.get('http://tinyurl.com/do101mtl')

#if (r.status_code == requests.codes.ok):

  #print(r.url)
  #print(r.headers)
  #print(r.content)
  #print(r.text)

  #la_page = r.text.encode('ascii', 'ignore')
  #print(la_page)
  #value = unicode(r.text, "utf-8")
  
  #print(r.encoding)
  #r.encoding = 'ISO-8859-1'
  #print(r.encoding)
  #soup = bs4.BeautifulSoup(la_page)
  #soup = BeautifulSoup(la_page, 'html.parser')
  #print(soup)
  
print('Fin du traitement')
  
  
  
  
