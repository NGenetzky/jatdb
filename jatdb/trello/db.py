
from tinydb import TinyDB
from tinydb import where

db = None

def get_db():
    global db
    if db is None:
        db = TinyDB('trello.json')
    return db

def get_table(name):
    d = get_db()
    return d.table(name)

def upsert(json,table):
    '''Wrapper around tinydb.upsert to default query to matching id'''
    return table.upsert(json, where('id') == json['id'])

