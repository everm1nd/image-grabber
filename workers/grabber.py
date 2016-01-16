import requests
from bs4 import BeautifulSoup
from workers.fetcher import fetch

def galleries_list(url):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    tags = soup.select('.phimage img')
    return [t.get('data-path') for t in tags]

def grab(url):
    galleries = galleries_list(url)
    print("Found images:", len(galleries))
    for gallery in galleries:
        fetch(gallery)
