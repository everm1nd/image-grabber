import urllib.request
import re
import hashlib
import os.path

def outname(url):
    return re.compile('(?:.+\/)([^#?]+)').findall(url)[0]

def outhashname(url):
    return hashlib.sha256(url.encode('utf-8')).hexdigest()

def fetch(url):
    hashname = outhashname(url)
    if not os.path.isfile(hashname):
        try:
            instream = urllib.request.urlopen(url)
        except urllib.error.HTTPError as error:
            print("HTTP Error: {0}".format(error), url)
            return
        output = open('./data/'+hashname, 'wb')
        output.write(instream.read())
        output.close()
        print("Downloaded: ", url)
