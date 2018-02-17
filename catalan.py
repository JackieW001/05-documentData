import pymongo
import json
from pprint import pprint

teamname = 'Cireres'

connection = pymongo.MongoClient("homer.stuy.edu")
db = connection[teamname]
collection = db['catalan']

filename = "catalan.json"
j = open(filename, 'r')

def parse_json (j):
    print type(j)
    return json.loads(j.replace('\r\n', ''))
    '''
    results = json['result']
    for line in result:
        print line
        print " "
    '''

print parse_json(j)

#collection.insert_one()

