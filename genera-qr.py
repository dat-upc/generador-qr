#!/usr/bin/env python3

import requests
import argparse
import qrcode
from bs4 import BeautifulSoup

# Configuro el parser d'arguments.
def doArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", "-u",
        type=str
    )
    parser.add_argument("--ext", "-e",
        type=str
    )
    return parser.parse_args()

if __name__ == "__main__":
    url = doArgs().url
    ext = doArgs().ext
    r = requests.get(url).text
    soup = BeautifulSoup(r, 'html.parser')
    for node in soup.find_all('a'):
        fitxer = node.get('href')
        if fitxer.endswith(ext):
            urlComplet = url + '/' + fitxer
            print (urlComplet)
            img = qrcode.make(urlComplet)
            img.save(fitxer[:fitxer.rfind('.')] + '.png')
