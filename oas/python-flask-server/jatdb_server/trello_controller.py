import connexion
import six

from jatdb_server.models.trello_query import TrelloQuery  # noqa: E501
from jatdb_server.models.universal_resource import UniversalResource  # noqa: E501
from jatdb_server import util


def trello_model_id_put(model, id):  # noqa: E501
    """Updates the models currently in db.

     # noqa: E501

    :param model: 
    :type model: str
    :param id: 
    :type id: str

    :rtype: UniversalResource
    """
    return 'do some magic!'


def trello_post(key=None, token=None, query=None):  # noqa: E501
    """trello_post

     # noqa: E501

    :param key: 
    :type key: str
    :param token: 
    :type token: str
    :param query: 
    :type query: dict | bytes

    :rtype: int
    """
    if connexion.request.is_json:
        query = TrelloQuery.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def trello_put(key=None, token=None):  # noqa: E501
    """trello_put

     # noqa: E501

    :param key: 
    :type key: str
    :param token: 
    :type token: str

    :rtype: int
    """
    return 'do some magic!'
