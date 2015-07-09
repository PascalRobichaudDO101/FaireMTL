
import csv
import time
import requests
import re

import BeautifulSoup

# Compteur pour identifier les projets
compteur = 0;

# Ouverture du fichier pour sauvegarder les donnees du scraping
output = open('donnees.csv', "w")
fdonnees = csv.writer(output, delimiter = ';')

r = requests.get('https://fairemtl.ca/fr/application-navigation-vers-stationnement-disponible')
# print(r.content)
soup = BeautifulSoup(r.content, 'html.parser')
print(soup.get_text())
print('Traitement complete')
