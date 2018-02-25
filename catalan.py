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

filename = "test.json"
f = open(filename,'r').read()

def join_duplicate_keys(ordered_pairs):
    d = {}
    for k, v in ordered_pairs:
        if k in d:
           if type(d[k]) == list:
               d[k].append(v)
           else:
               newlist = []
               newlist.append(d[k])
               newlist.append(v)
               d[k] = newlist
        else:
           d[k] = v
    return d

newdict = json.loads(f, object_pairs_hook=join_duplicate_keys)

el = newdict['result']

print el




#Adding to Database
#collection.insert_many(el)

'''
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
