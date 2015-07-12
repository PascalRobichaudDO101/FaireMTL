# coding: utf8

import urllib
from bs4 import BeautifulSoup

# Page à scraper
#source_url = 'https://fairemtl.ca/fr/affichage-dynamique-vers-stationnement-disponible'
source_url = 'https://fairemtl.ca/fr/24h-linnovation-volet-ville-intelligente'
print('-'*60)
print("Page: %s" % source_url)
html = urllib.urlopen(source_url)

#Mettre la code de la page dans BeautifulSoup
soup = BeautifulSoup(html)

# 1. Nombre de commentaires
onglet_commentaires = soup.find("a",{"href":"#tabs-0-footer-2"})
onglet_commentaires = onglet_commentaires.getText()
onglet_commentaires = onglet_commentaires.replace("Commentaires (","")
onglet_commentaires = onglet_commentaires.replace(")","")

# Afficher le nombre de commentaire
print("Nombre de commentaires: %s" % onglet_commentaires)	   

  
print('Fin du traitement')
  
  
  
  
