#!/usr/bin/env python3
# A script to get latest movies, trailers and ratings
import json
from urllib import request
import requests
from datetime import datetime
from bs4 import BeautifulSoup
from os import path

# Paths
basepath = path.dirname(__file__)
ledpath = path.abspath(path.join(basepath, "..", "hledger.journal"))

URL="https://www.imccinemas.ie/Whats-On/Athlone"
API_URL="https://www.imccinemas.ie/DesktopModules/Inventise.IMC.API/V1/API/Search/"

def get_data(session, url):
    result = session.get(url)
    return BeautifulSoup(result.content,"html.parser")

def post_data(session, url, data):
    result = session.post(url, data=data)
    return BeautifulSoup(result.content,"html.parser")

def get_json(url):
    with request.urlopen(url) as resp:
        data = json.loads(resp.read().decode())
        return data

def post_json(body, url):
    jsondata = json.dumps(body)
    jsonbytes = jsondata.encode('utf-8')
    req = request.Request(url)
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    req.add_header('Content-Length', len(jsonbytes))
    resp = json.loads(request.urlopen(req, jsonbytes).read().decode())
    return resp


def get_movies_on():
    session_requests = requests.session()
    soup = get_data(session_requests, URL)
    print(soup)

def get_movies_list():
    url = API_URL + "GetEventsByVenueDescription"
    body = { "description": "Athlone" }
    resp = post_json(body, url)
    for i in resp['data']:
        print(i)

def main():
    #get_movies_on()
    get_movies_list()
    d = []
    dpath = path.join(basepath, "data", "data.json")
    with open(dpath, 'w') as fp:
        json.dump(d, fp)


if __name__ == '__main__':
    main()
