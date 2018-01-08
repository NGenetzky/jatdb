
from json import dump
from json import load
from tinydb import TinyDB
from tinydb import where

db = None

FILES = {
    'db': 'trello.db.json',
    'saved': 'trello.json',
}

def get_db():
    global db
    if db is None:
        db = TinyDB(FILES['db'])
    return db

def get_table(name):
    d = get_db()
    return d.table(name)

def upsert(json,table):
    '''Wrapper around tinydb.upsert to default query to matching id'''
    return table.upsert(json, where('id') == json['id'])

def save_db():
    j = {}
    with open(FILES['db'], 'r') as f:
        j = load(f)
    with open(FILES['saved'], 'w') as f:
        dump(j, f, sort_keys=True, indent='\t')

def main(args=None):
    save_db()

if __name__ == "__main__":
    import sys
    sys.exit(main(sys.argv[1:]))

