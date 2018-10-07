# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from jatdb_server.models.trello_query import TrelloQuery  # noqa: E501
from jatdb_server.models.universal_resource import UniversalResource  # noqa: E501
from jatdb_server.test import BaseTestCase


class TestTrelloController(BaseTestCase):
    """TrelloController integration test stubs"""

    def test_trello_model_id_put(self):
        """Test case for trello_model_id_put

        Updates the models currently in db.
        """
        response = self.client.open(
            '/v0/trello/{model}/{id}'.format(model='model_example', id='id_example'),
            method='PUT',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_trello_post(self):
        """Test case for trello_post

        
        """
        query = TrelloQuery()
        query_string = [('key', 'key_example'),
                        ('token', 'token_example')]
        response = self.client.open(
            '/v0/trello/',
            method='POST',
            data=json.dumps(query),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_trello_put(self):
        """Test case for trello_put

        
        """
        query_string = [('key', 'key_example'),
                        ('token', 'token_example')]
        response = self.client.open(
            '/v0/trello/',
            method='PUT',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
