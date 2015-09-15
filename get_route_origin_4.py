#!/bin/python 

import json
import requests
from pprint import pprint
import sys

AS = sys.argv[1]

BASE_URL = 'http://rest.db.ripe.net/search'

def get_route_origin_4(ASN):
    r =  requests.get(BASE_URL, headers= {'Accept' : 'application/json'}, params={'inverse-attribute': 'origin','query-string': ASN})
    j = json.loads(r.text)
    z = []
    try:
        j['errormessages']
    except: 
        for i in j['objects']['object']:
            if i['attributes']['attribute'][0]['name'] == 'route':
               print(i['attributes']['attribute'][0]['value'])   
        
get_route_origin_4(AS)
 
