import connexion
import six

from jatdb_server.models.universal_resource import UniversalResource  # noqa: E501
from jatdb_server import util

# oas import above, mine below

import tinydb

from jatdb_server.data.tinydb_handler import get_db

def uri_post(uri):  # noqa: E501
    """uri_post

     # noqa: E501

    :param uri: 
    :type uri: dict | bytes

    :rtype: UniversalResource
    """
    if connexion.request.is_json:
        uri = UniversalResource.from_dict(connexion.request.get_json())  # noqa: E501

    db = get_db()
    t = db.table('jatdb.universal_resource')

    query = tinydb.Query()
    docs = db.search(query.uri == uri.uri)

    if len(docs) is 0:
        data = {
            "uri":uri.uri,
            "uuid":uri.uuid,
            "date":uri.date
        }
        docid = t.insert(data)
        rv = uri
    elif len(docs) is 1:
        rv = UniversalResource.from_dict(docs[0])
    else:
        raise Exception('There should never be more than one doc!')

    return rv
