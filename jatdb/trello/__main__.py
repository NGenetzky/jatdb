import sys

from jatdb.trello.client import get_client
from jatdb.trello.db import get_table
from jatdb.trello.db import upsert
from jatdb.trello.db import upsert_board
from jatdb.trello.json import board_to_json
from jatdb.trello.json import list_to_json

def main(args=None):
    c = get_client()

    boards = c.list_boards()
    for b in boards:
        j = board_to_json(b)
        upsert_board(j)

        list_table = get_table('lists')
        lists = b.get_lists('all')
        for l in lists:
            upsert(list_to_json(l), list_table)

    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
