#!/usr/bin/env python
'''Provides access to the Trello REST API via py-trello'''

import trello
import trello.util

from jatdb.secret import get_secret

SECRETS = get_secret('trello')

def create_oauth_token():
    return trello.util.create_oauth_token(
        key=get_secret('trello','api_key'),
        secret=get_secret('trello','api_secret')
        )

def get_client():
    return trello.TrelloClient(
        api_key=SECRETS['api_key'],
        api_secret=SECRETS['api_key'],
        token=SECRETS['token'],
        token_secret=SECRETS['token_secret']
        )

def main(args=None):
    client = get_client()
    boards = client.list_boards()
    for b in boards:
        print('\t{}'.format(b))
        lists = b.list_lists()
        for l in lists:
            print('\t\t{}'.format(l))
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main(sys.argv[1:]))

