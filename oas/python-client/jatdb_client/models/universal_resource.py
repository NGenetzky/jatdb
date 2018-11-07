# coding: utf-8

"""
    jatdb

    JSON API to DB: Fetch JSON from APIs and send to a TinyDB database.  # noqa: E501

    OpenAPI spec version: 0.0.2
    Contact: Nathan@Genetzky.us
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class UniversalResource(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'uri': 'str',
        'uuid': 'str',
        'date': 'date'
    }

    attribute_map = {
        'uri': 'uri',
        'uuid': 'uuid',
        'date': 'date'
    }

    def __init__(self, uri=None, uuid=None, date=None):  # noqa: E501
        """UniversalResource - a model defined in Swagger"""  # noqa: E501

        self._uri = None
        self._uuid = None
        self._date = None
        self.discriminator = None

        self.uri = uri
        if uuid is not None:
            self.uuid = uuid
        if date is not None:
            self.date = date

    @property
    def uri(self):
        """Gets the uri of this UniversalResource.  # noqa: E501


        :return: The uri of this UniversalResource.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this UniversalResource.


        :param uri: The uri of this UniversalResource.  # noqa: E501
        :type: str
        """
        if uri is None:
            raise ValueError("Invalid value for `uri`, must not be `None`")  # noqa: E501

        self._uri = uri

    @property
    def uuid(self):
        """Gets the uuid of this UniversalResource.  # noqa: E501


        :return: The uuid of this UniversalResource.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this UniversalResource.


        :param uuid: The uuid of this UniversalResource.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def date(self):
        """Gets the date of this UniversalResource.  # noqa: E501


        :return: The date of this UniversalResource.  # noqa: E501
        :rtype: date
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this UniversalResource.


        :param date: The date of this UniversalResource.  # noqa: E501
        :type: date
        """

        self._date = date

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UniversalResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
