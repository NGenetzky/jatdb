import sys

from jatdb.trello.client import get_client
from jatdb.trello.data import Data
from jatdb.trello.db import get_db
from jatdb.trello.db import get_table
from jatdb.trello.db import upsert
from jatdb.trello.json import board_to_json
from jatdb.trello.json import card_to_json
from jatdb.trello.json import list_to_json

def upsert_boards_from_client(c):
    boards_table = get_table('boards')
    boards = c.list_boards()
    for b in boards:
        upsert(board_to_json(b), boards_table)

def upsert_lists_from_board(b):
    lists_table = get_table('lists')
    lists = b.get_lists('all')
    for l in lists:
        upsert(list_to_json(l), lists_table)

def upsert_cards_from_list(l):
    cards_table = get_table('cards')
    cards = l.list_cards('all')
    for card in cards:
        upsert(card_to_json(card), cards_table)

def tinydb_to_data(db, d):
    for j in db.table('boards'):
        d.add_board(j)
    for j in db.table('lists'):
        d.add_list(j)
    for j in db.table('cards'):
        d.add_card(j)

def do_tinydb_to_data():
    db = get_db()
    d = Data('_data')
    tinydb_to_data(db,d)

def do_client_to_tinydb():
    c = get_client()

    upsert_boards_from_client(c)
    for b in c.list_boards():
        upsert_lists_from_board(b)
        for l in b.get_lists('all'):
            upsert_cards_from_list(l)

    return 0

def do_client_to_data():
    c = get_client()
    boards = c.list_boards()

    d = Data('_data')
    for b in boards:
        d.add_board(board_to_json(b))
        for l in b.get_lists('all'):
            d.add_list(list_to_json(l))
            for card in l.list_cards('all'):
                d.add_card(card_to_json(card))

def main(args=None):
    # return do_client_to_data()
    do_client_to_tinydb()
    return do_tinydb_to_data()

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
