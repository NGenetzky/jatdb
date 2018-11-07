# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from jatdb_server.models.content_file import ContentFile  # noqa: E501
from jatdb_server.models.universal_resource import UniversalResource  # noqa: E501
from jatdb_server.test import BaseTestCase


class TestContentController(BaseTestCase):
    """ContentController integration test stubs"""

    def test_content_get(self):
        """Test case for content_get

        
        """
        query_string = [('path', 'path_example')]
        response = self.client.open(
            '/content/',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_content_post(self):
        """Test case for content_post

        
        """
        contentfile = ContentFile()
        response = self.client.open(
            '/content/',
            method='POST',
            data=json.dumps(contentfile),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_content_put(self):
        """Test case for content_put

        
        """
        contentfile = ContentFile()
        query_string = [('path', 'path_example')]
        response = self.client.open(
            '/content/',
            method='PUT',
            data=json.dumps(contentfile),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
