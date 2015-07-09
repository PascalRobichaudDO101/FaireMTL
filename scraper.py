
import csv
import time
import requests
import re

import BeautifulSoup

#Compteur pour identifier les projets
compteur = 0;

#Ouverture du fichier pour sauvegarder les données du scraping
output = open('donnees.csv', "w")
fdonnees = csv.writer(output, delimiter = ';')

print('Traitement complété')
