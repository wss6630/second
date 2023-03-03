import requests
import json
from requests.auth import HTTPDigestAuth
from bs4 import BeautifulSoup

r = requests.get('https://bits.media/difficulty/bitcoin/')
soup = BeautifulSoup (r.text, 'lxml')

r = requests.get('https://bits.media/difficulty/bitcoin/')

print(r.status_code)
print(r.text)
