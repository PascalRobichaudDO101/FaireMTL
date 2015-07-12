# coding: utf8

#Scraper pour le site FaireMTl.ca
#Version 3.0, 2015-07-12

#Fonction left
def left(s, amount = 1, substring = ""):
    if (substring == ""):
        return s[:amount]
    else:
        if (len(substring) > amount):
           substring = substring[:amount]
        return substring + s[:-amount]

from datetime import datetime, date, time
import sqlite3
import urllib
from bs4 import BeautifulSoup

traitement_debut = datetime.now() 
print("Début du traitement: %s " % traitement_debut)

# Page à scraper
#source_url = 'https://fairemtl.ca/fr/affichage-dynamique-vers-stationnement-disponible'
source_url = 'https://fairemtl.ca/fr/24h-linnovation-volet-ville-intelligente'
print("Page: %s" % source_url)
html = urllib.urlopen(source_url)

#Mettre la code de la page dans BeautifulSoup
soup = BeautifulSoup(html)

# 1. Nombre de commentaires
onglet_commentaires = soup.find("a",{"href":"#tabs-0-footer-2"})
onglet_commentaires = onglet_commentaires.getText()
onglet_commentaires = onglet_commentaires.replace("Commentaires (","")
onglet_commentaires = onglet_commentaires.replace(")","")

# Afficher le nombre de commentaires
print("Nombre de commentaires: %s" % onglet_commentaires)	   

#2. Nombre d'abonnés
nombre_abonnes = soup.find_all('div',{'class':'pill js-subscribe_section_content'})
#print("Nombre d'abonnés:       %s" % nombre_adonnes)
#foutput_debug.writerow(nombre_adonnes)             
nombre_adonnes2 = nombre_abonnes[0].getText().strip()
position_espace = nombre_adonnes2.find(' ')
nombre_adonnes2 = left(nombre_adonnes2, position_espace - 1)
#print("Nombre d'abonnés:       %s" % nombre_adonnes2)
print("Nombre de abonnes:      %s" % nombre_adonnes2)
#print(nombre_adonnes2)
  
#3. Nombre d'appuis
nombre_appuis = soup.find_all('div',{'class':'pill js-support_project'})
#print("Nombre d'appuis:        %s" % nombre_appuis)
#foutput_debug.writerow(nombre_appuis) 
nombre_appuis2 = nombre_appuis[0].getText().strip()
position_espace = nombre_appuis2.find(' ')
nombre_appuis2 = left(nombre_appuis2, position_espace - 1)
print("Nombre d'appuis:        %s" % nombre_appuis2)

#Fin du traitement
traitement_fin = datetime.now() 
print("Fin du traitement: %s " % traitement_fin)

traitement_duree = traitement_fin - traitement_debut
print("Durée du traitement: %s" % traitement_duree)
  
  
