import urllib.request
import re
import hashlib
import os.path

def outname(url):
    return re.compile('(?:.+\/)([^#?]+)').findall(url)[0]

def outhashname(url):
    return hashlib.sha256(url.encode('utf-8')).hexdigest()

def image_links(gallery):
    links = []
    regex = re.compile(r"{index}")
    for i in range(0,16):
        links.append(regex.sub(str(i+1), gallery))
    return links

def fetch(gallery_url_template):
    for link in image_links(gallery_url_template):
        hashname = outhashname(link)
        if not os.path.isfile(hashname):
            try:
                instream = urllib.request.urlopen(link)
            except urllib.error.HTTPError as error:
                print("HTTP Error: {0}".format(error), link)
                return
            output = open('./data/'+hashname, 'wb')
            output.write(instream.read())
            output.close()
            print("Downloaded: ", link)
