import pymongo
import json
from pprint import pprint

teamname = 'Cireres'

connection = pymongo.MongoClient("homer.stuy.edu")
db = connection[teamname]
collection = db['catalan']

filename = "catalan.json"

def parse_json (filename):
    
    with open(filename) as json_data:
       d = json.load(json_data)
    return d['result']

pprint(parse_json(filename))

#collection.insert_one()

