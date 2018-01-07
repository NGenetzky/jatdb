import sys

from jatdb.trello.client import get_client
from jatdb.trello.db import get_db
from jatdb.trello.db import upsert_board
from jatdb.trello.json import board_to_json

def main(args=None):
    db = get_db()
    c = get_client()

    boards = c.list_boards()
    for b in boards:
        j = board_to_json(b)
        upsert_board(j)

    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
