# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from jatdb_server.models.base_model_ import Model
from jatdb_server import util


class TrelloQuery(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, uri=None, query_append=None):  # noqa: E501
        """TrelloQuery - a model defined in Swagger

        :param uri: The uri of this TrelloQuery.  # noqa: E501
        :type uri: str
        :param query_append: The query_append of this TrelloQuery.  # noqa: E501
        :type query_append: str
        """
        self.swagger_types = {
            'uri': str,
            'query_append': str
        }

        self.attribute_map = {
            'uri': 'uri',
            'query_append': 'query_append'
        }

        self._uri = uri
        self._query_append = query_append

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The TrelloQuery of this TrelloQuery.  # noqa: E501
        :rtype: TrelloQuery
        """
        return util.deserialize_model(dikt, cls)

    @property
    def uri(self):
        """Gets the uri of this TrelloQuery.


        :return: The uri of this TrelloQuery.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this TrelloQuery.


        :param uri: The uri of this TrelloQuery.
        :type uri: str
        """

        self._uri = uri

    @property
    def query_append(self):
        """Gets the query_append of this TrelloQuery.

        Extra query information  # noqa: E501

        :return: The query_append of this TrelloQuery.
        :rtype: str
        """
        return self._query_append

    @query_append.setter
    def query_append(self, query_append):
        """Sets the query_append of this TrelloQuery.

        Extra query information  # noqa: E501

        :param query_append: The query_append of this TrelloQuery.
        :type query_append: str
        """

        self._query_append = query_append
