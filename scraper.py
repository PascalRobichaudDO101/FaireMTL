import time
import urllib
import re
import csv


HTML = urllib.urlopen("http://fairemtl.ca").read()
HTML = re.search('<h1>', HTML, re.S)
print(HTML)

print('Fin du traitement')
