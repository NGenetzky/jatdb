
def board_to_json(o):
    '''Converts trello.board.Board to json

    https://developers.trello.com/v1.0/reference#board-object
    {
      "id": "586e8f681d4fe9b06a928307",
      "name": "Best Test Board!",
      "desc": "",
      "descData": null,
      "closed": false,
      "idOrganization": "586e8d7b1af892b26d5b76b1",
      "pinned": false,
      "url": "https://trello.com/b/d2EnEWSY/best-test-board",
      "shortUrl": "https://trello.com/b/d2EnEWSY",
      "prefs": {...},
      "labelNames": {...}
    }
    '''
    d = {
        'id': o.id,
        'name': o.name,
        'desc': o.description,
        'closed': o.closed,
        # 'idOrganization': o.client.id, # TODO: This doesn't seem to be available?
        'url': o.url,
    }
    return d

def list_to_json(o):
    '''Converts trello.trellolist.List to json

    https://developers.trello.com/v1.0/reference#list-object
    {
      "id": "560bf48efe2771efe9b45997",
      "name": "Washington",
      "closed": false,
      "idBoard": "560bf4298b3dda300c18d09c",
      "pos": 1638399,
      "subscribed": false
    }
    '''
    d = {
        'id': o.id,
        'name': o.name,
        'closed': o.closed,
        'idBoard': o.board.id,
        'pos': o.pos,
    }
    return d

