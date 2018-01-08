
import json

def dump(obj, fp):
    json.dump(obj, fp, sort_keys=True, indent='\t')

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
        # 'dateLastActivity': o.date_last_activity.isoformat(), # TODO
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

def card_to_json(o):
    '''Converts trello.trellolist.Card to json

    https://developers.trello.com/v1.0/reference#card-object
    {
      "id": "560bf4dd7139286471dc009c",
      "badges": {...},
      "checkItemStates": [ ],
      "closed": false,
      "dueComplete": false,
      "dateLastActivity": "2017-06-26T17:39:49.583Z",
      "desc": "",
      "descData": null,
      "due": null,
      "email": null,
      "idBoard": "560bf4298b3dda300c18d09c",
      "idChecklists": [ ],
      "idList": "560bf44ea68b16bd0fc2a9a9",
      "idMembers": [ "556c8537a1928ba745504dd8" ],
      "idMembersVoted": [ ],
      "idShort": 9,
      "idAttachmentCover": "5944a06460ed0bee471ad8e0",
      "manualCoverAttachment": false,
      "labels": [ ],
      "idLabels": [ "560bf42919ad3a5dc29f33c5" ],
      "name": "Grand Canyon National Park",
      "pos": 16384,
      "shortLink": "nqPiDKmw",
      "shortUrl": "https://trello.com/c/nqPiDKmw",
      "subscribed": true,
      "url": "https://trello.com/c/nqPiDKmw/9-grand-canyon-national-park"
    }
    '''

    d = {
        'closed': o.closed,
        'dateLastActivity': o.dateLastActivity.isoformat(),
        'desc': o.desc,
        'due': o.due,
        'id': o.id,
        'idBoard': o.idBoard,
        'idLabels': o.idLabels,
        'idList': o.idList,
        'idMembers': o.idMembers,
        'idShort': o.idShort,
        'pos': o.pos,
        'shortUrl': o.shortUrl,
        'url': o.url,
    }
    return d


