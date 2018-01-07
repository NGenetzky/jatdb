
def board_to_json(b):
    d = {}
    d['id'] = b.id
    d['name'] = b.name
    d['url'] = b.url
    # d['dateLastActivity'] = b.date_last_activity # TODO
    d['desc'] = b.description
    return d

def list_to_json(o):
    '''Converts trello.List to json

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
        # 'subscribed': o.subscribed,
    }
    return d

