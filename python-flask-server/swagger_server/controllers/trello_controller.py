import connexion
from swagger_server.models.trello_query import TrelloQuery
from swagger_server.models.universal_resource import UniversalResource
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime

from tinydb import where
from tinydb import TinyDB
from trello import TrelloClient

import requests
import json

JSONDB = '/data/db.json'

def table_name(model):
    return 'trello.{0}'.format(model)

def trello_model_id_put(model, id, key, token):
    """
    trello_model_id_put
    
    :param model: 
    :type model: str
    :param id: 
    :type id: str
    :param key: 
    :type key: str
    :param token: 
    :type token: str

    :rtype: UniversalResource
    """

    url = "https://api.trello.com/1/{0}/{1}".format(model, id)
    querystring = {
        "key": key,
        "token": token
    }
    response = requests.request("GET", url, params=querystring)

    if response.status_code not in [200]:
        return (response.status_code, response.text)
    j = json.loads(response.text)

    db = TinyDB(JSONDB)
    t = db.table(table_name(model))
    t.upsert(j, where('id') == j['id'])

    return response.text


def trello_post(key, token, query=None):
    """
    trello_post
    
    :param key: 
    :type key: str
    :param token: 
    :type token: str
    :param query: 
    :type query: dict | bytes

    :rtype: int
    """
    if connexion.request.is_json:
        query = TrelloQuery.from_dict(connexion.request.get_json())
    return 'do some magic!'


def trello_put(key, token):
    """
    trello_put
    
    :param key: 
    :type key: str
    :param token: 
    :type token: str

    :rtype: int
    """
    c = TrelloClient( api_key=key, token=token )
    boards = c.list_boards()
    return ' '.join(boards)

