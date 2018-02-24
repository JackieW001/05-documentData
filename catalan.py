'''
Name: Catalan Historical Events Dataset
Our dataset contains the date and the event that occured on that date in the Catalan language. For example, the second entry of this dataset states that in the year -300, the first documented meteorological forecast was written by Teofrasto. 

Hyperlink: 
http://www.vizgr.org/historical-events/search.php?format=json&begin_date=-3000000&end_date=20151231&lang=ca

Import mechanism:
We made each event a separate collection in the Cieres database.

'''

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

'''
#Adding to Database
collection.insert_many(parse_json) #parse_json should return list of documents and each new document is defined by the "event" key. i.e. "event": {"date": "-300", "description": "Auge de Meroe", "lang": "ca", "granularity": "year"} and "event": {"date": "-300", "description": "Primera publicaci\u00f3 d'una previsi\u00f3 meteorol\u00f2gica documentada (obra de Teofrast)" will be two separate documents

#Searching by date
def date(d):
    c = collection.find({'event.date':d})
    for i in c:
        print i
date('-300')


def desc(d):
    c = collection.find({'event.description':d})
    for i in c:
        print i
desc('Auge de Mero')


def gran(g):
    c = collection.find({'event.granularity':g})
    for i in c:
        print i
gran('year')


def lang(l):
    c = collection.find({'event.lang':l})
    for i in c:
        print i
lang('ca')
'''
