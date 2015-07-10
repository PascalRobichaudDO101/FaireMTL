# coding: utf8

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
html = html.decode('utf8')
soup = BeautifulSoup(html)
#print(soup.prettify())

projet = soup.find("title")
print(projet.getText())

description = soup.find("div",{"class":"field field-name-body field-type-text-with-summary field-label-hidden"})
print(description)

onglet_commentaires = soup.find("a",{"href":"#tabs-0-footer-2"})

#Extraire le chiffre du libellé de l'onglet

#Afficher le nombre de commentaire (pour du débuggage)
print("Nombre de commentaires: %s" % onglet_commentaires)	   



    
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
  
  
  
  
