import time
import urllib
import re
import csv
import tweepy

HTML = urllib.urlopen("http://fairemtl.ca").read()
HTML = re.search('<h1>', HTML, re.S)
print(HTML)
