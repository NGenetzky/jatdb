# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from jatdb_server.models.base_model_ import Model
from jatdb_server import util


class ContentFile(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, content=None, path=None, metadata=None):  # noqa: E501
        """ContentFile - a model defined in Swagger

        :param content: The content of this ContentFile.  # noqa: E501
        :type content: str
        :param path: The path of this ContentFile.  # noqa: E501
        :type path: str
        :param metadata: The metadata of this ContentFile.  # noqa: E501
        :type metadata: object
        """
        self.swagger_types = {
            'content': str,
            'path': str,
            'metadata': object
        }

        self.attribute_map = {
            'content': 'content',
            'path': 'path',
            'metadata': 'metadata'
        }

        self._content = content
        self._path = path
        self._metadata = metadata

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ContentFile of this ContentFile.  # noqa: E501
        :rtype: ContentFile
        """
        return util.deserialize_model(dikt, cls)

    @property
    def content(self):
        """Gets the content of this ContentFile.

        Actual markdown content  # noqa: E501

        :return: The content of this ContentFile.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this ContentFile.

        Actual markdown content  # noqa: E501

        :param content: The content of this ContentFile.
        :type content: str
        """
        if content is None:
            raise ValueError("Invalid value for `content`, must not be `None`")  # noqa: E501

        self._content = content

    @property
    def path(self):
        """Gets the path of this ContentFile.

        Relative path to file  # noqa: E501

        :return: The path of this ContentFile.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this ContentFile.

        Relative path to file  # noqa: E501

        :param path: The path of this ContentFile.
        :type path: str
        """

        self._path = path

    @property
    def metadata(self):
        """Gets the metadata of this ContentFile.

        Data associated with content  # noqa: E501

        :return: The metadata of this ContentFile.
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this ContentFile.

        Data associated with content  # noqa: E501

        :param metadata: The metadata of this ContentFile.
        :type metadata: object
        """

        self._metadata = metadata
