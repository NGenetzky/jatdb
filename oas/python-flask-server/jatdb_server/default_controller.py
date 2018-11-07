import connexion
import six

from jatdb_server.models.universal_resource import UniversalResource  # noqa: E501
from jatdb_server import util


def uri_post(uri):  # noqa: E501
    """uri_post

     # noqa: E501

    :param uri: 
    :type uri: dict | bytes

    :rtype: UniversalResource
    """
    if connexion.request.is_json:
        uri = UniversalResource.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
