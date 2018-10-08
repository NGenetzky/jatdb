import connexion
import six

from jatdb_server.models.content_file import ContentFile  # noqa: E501
from jatdb_server.models.universal_resource import UniversalResource  # noqa: E501
from jatdb_server import util

# oas import above, mine below

import tinydb

from jatdb_server.data.tinydb_handler import DbApp

def content_get(path):  # noqa: E501
    """content_get

     # noqa: E501

    :param path: Relative path to file
    :type path: str

    :rtype: ContentFile
    """
    return 'do some magic!'


def content_post(contentfile):  # noqa: E501
    """content_post

     # noqa: E501

    :param contentfile: 
    :type contentfile: dict | bytes

    :rtype: UniversalResource
    """
    if connexion.request.is_json:
        contentfile = ContentFile.from_dict(connexion.request.get_json())  # noqa: E501

    dbapp = DbApp()
    ret = dbapp.post_content(contentfile)

    return ret


def content_put(path, contentfile):  # noqa: E501
    """content_put

     # noqa: E501

    :param path: Relative path to file
    :type path: str
    :param contentfile: 
    :type contentfile: dict | bytes

    :rtype: UniversalResource
    """
    if connexion.request.is_json:
        contentfile = ContentFile.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
