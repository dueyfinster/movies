#!/usr/bin/env python3
import json
import requests
from datetime import datetime
from bs4 import BeautifulSoup
from os import path

# Paths
basepath = path.dirname(__file__)
ledpath = path.abspath(path.join(basepath, "..", "hledger.journal"))

URL="https://www.imccinemas.ie/Whats-On/Athlone"

def get_data(session, url):
    result = session.get(url)
    return BeautifulSoup(result.content,"html.parser")

def post_data(session, url, data):
    result = session.post(url, data=data)
    return BeautifulSoup(result.content,"html.parser")

def get_movies_on():
  session_requests = requests.session()
  soup = get_data(session_requests, URL)
  print(soup)



def main():
    d = []
    dpath = path.join(basepath, "data", "data.json")
    with open(dpath, 'w') as fp:
        json.dump(d, fp)


if __name__ == '__main__':
    main()
