# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from jatdb_server.models.base_model_ import Model
from jatdb_server import util


class UniversalResource(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    swagger_types = {
        'uri': str,
        'uuid': str,
        'date': date
    }

    attribute_map = {
        'uri': 'uri',
        'uuid': 'uuid',
        'date': 'date'
    }

    def __init__(self, uri=None, uuid=None, date=None):  # noqa: E501
        """UniversalResource - a model defined in Swagger

        :param uri: The uri of this UniversalResource.  # noqa: E501
        :type uri: str
        :param uuid: The uuid of this UniversalResource.  # noqa: E501
        :type uuid: str
        :param date: The date of this UniversalResource.  # noqa: E501
        :type date: date
        """
        self._uri = uri
        self._uuid = uuid
        self._date = date

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The UniversalResource of this UniversalResource.  # noqa: E501
        :rtype: UniversalResource
        """
        return util.deserialize_model(dikt, cls)

    @property
    def uri(self):
        """Gets the uri of this UniversalResource.


        :return: The uri of this UniversalResource.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this UniversalResource.


        :param uri: The uri of this UniversalResource.
        :type uri: str
        """
        if uri is None:
            raise ValueError("Invalid value for `uri`, must not be `None`")  # noqa: E501

        self._uri = uri

    @property
    def uuid(self):
        """Gets the uuid of this UniversalResource.


        :return: The uuid of this UniversalResource.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this UniversalResource.


        :param uuid: The uuid of this UniversalResource.
        :type uuid: str
        """

        self._uuid = uuid

    @property
    def date(self):
        """Gets the date of this UniversalResource.


        :return: The date of this UniversalResource.
        :rtype: date
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this UniversalResource.


        :param date: The date of this UniversalResource.
        :type date: date
        """

        self._date = date
