# coding: utf-8

"""
    NGenetzky's API

    This is an API I am designing for myself using swagger. You can find  out more about Swagger at [http://swagger.io](http://swagger.io)   # noqa: E501

    OpenAPI spec version: 0.0.1
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
