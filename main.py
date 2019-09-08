#!/usr/bin/env python3
# A script to get latest movies, trailers and ratings
import json
from urllib import request
from urllib.parse import quote
from pprint import pprint
from datetime import datetime
from os import path

# Paths
basepath = path.dirname(__file__)

URL="https://www.imccinemas.ie/Whats-On/Athlone"
API_URL="https://www.imccinemas.ie/DesktopModules/Inventise.IMC.API/V1/API/Search/"
IMG_URL="https://www.imccinemas.ie/Portals/0/EventImages/"
LOC="Athlone"
OMDB_API_KEY="f4a055f7"

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


def get_movies_list():
    url = API_URL + "GetEventsByVenueDescription"
    body = { "description": LOC }
    resp = post_json(body, url)
    nd = []
    for m in resp['data']:
        img_url = IMG_URL + m['Image']
        nd.append({"id": m['UrlLink'], "title": m['Description'], "description": m['EventSummary'],"image": img_url, "release-date": m['ReleaseDate'], "director": m['Director'], "starring": m['Staring'], "duration": m['Duration'], "age-rating": m['RatingIE'], "trailer": m['Trailer'], "url": m['UrlLink']})
    return nd


def get_movie_times(movies):
    url = API_URL + "GetEventDatesAndPerformances"
    for m in movies:
        body = { "eventDescription": m['id'], "eventDate": None, "venueDescription": LOC }
        resp = post_json(body, url)['data']
        evd = []
        for ed in resp['EventDates']:
            times = []
            for st in ed['PerformanceDetails']:
                times.append({"time": st['StartDate'], "screen": st['ScreenNumber']})
            evd.append({"date": ed['EventDate'], "times": times})
        m['showtimes'] = evd
    return movies

def get_movie_ratings(movies):
    for m in movies:
        mtitle = quote(m['title'])
        yr = datetime.strptime(m['release-date'], "%Y-%m-%dT%H:%M:%S").year
        url = f'http://www.omdbapi.com/?t={mtitle}&type=movie&y={yr}&apikey={OMDB_API_KEY}'
        resp = get_json(url)
        if 'Error' not in resp:
            m['ratings'] = resp['Ratings']
    return movies

def main():
    movies = get_movies_list()
    movies = get_movie_times(movies)
    d = get_movie_ratings(movies)
    dpath = path.join(basepath, "data", "data.json")
    with open(dpath, 'w') as fp:
        json.dump(d, fp)


if __name__ == '__main__':
    main()
