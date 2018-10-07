import connexion
import six

from jatdb_server.models.universal_resource import UniversalResource  # noqa: E501
from jatdb_server import util

# oas import above, mine below

import tinydb

from jatdb_server.data.tinydb_handler import DbApp

def uri_post(uri):  # noqa: E501
    """uri_post

     # noqa: E501

    :param uri: 
    :type uri: dict | bytes

    :rtype: UniversalResource
    """
    if connexion.request.is_json:
        uri = UniversalResource.from_dict(connexion.request.get_json())  # noqa: E501

    dbapp = DbApp()
    table = dbapp.db.table('jatdb.universal_resource')

    query = tinydb.Query()
    docs = table.search(query.uri == uri.uri)

    if len(docs) is 0:
        docid = table.insert(uri.to_dict())
        rv = uri
    elif len(docs) is 1:
        rv = UniversalResource.from_dict(docs[0])
    else:
        raise Exception('There should never be more than one doc!')

    return rv
