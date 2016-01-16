import requests
import re
from bs4 import BeautifulSoup
from workers.fetcher import fetch

def absolute_url(url,base):
    if re.compile('^http').match(url):
        return url
    else:
        return url+base

def images_list(url):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    tags = soup.find_all('img')
    return [t.get('src') for t in tags]

def grab(url):
    images = images_list(url)
    print("Found images:", len(images))
    for image in images:
        fetch(absolute_url(image,url))
