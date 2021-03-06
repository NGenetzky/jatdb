# coding: utf-8

"""
    jatdb

    JSON API to DB: Fetch JSON from APIs and send to a TinyDB database.  # noqa: E501

    OpenAPI spec version: 0.0.2
    Contact: Nathan@Genetzky.us
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import jatdb_client
from jatdb_client.api.trello_api import TrelloApi  # noqa: E501
from jatdb_client.rest import ApiException


class TestTrelloApi(unittest.TestCase):
    """TrelloApi unit test stubs"""

    def setUp(self):
        self.api = jatdb_client.api.trello_api.TrelloApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_trello_model_id_put(self):
        """Test case for trello_model_id_put

        Updates the models currently in db.  # noqa: E501
        """
        pass

    def test_trello_post(self):
        """Test case for trello_post

        """
        pass

    def test_trello_put(self):
        """Test case for trello_put

        """
        pass


if __name__ == '__main__':
    unittest.main()
