# coding: utf-8

"""
    NGenetzky's API

    This is an API I am designing for myself using swagger. You can find  out more about Swagger at [http://swagger.io](http://swagger.io)   # noqa: E501

    OpenAPI spec version: 0.0.1
    Contact: Nathan@Genetzky.us
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from jatdb_client.api_client import ApiClient


class TrelloApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def trello_model_id_put(self, model, id, **kwargs):  # noqa: E501
        """Updates the models currently in db.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.trello_model_id_put(model, id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str model: (required)
        :param str id: (required)
        :return: UniversalResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.trello_model_id_put_with_http_info(model, id, **kwargs)  # noqa: E501
        else:
            (data) = self.trello_model_id_put_with_http_info(model, id, **kwargs)  # noqa: E501
            return data

    def trello_model_id_put_with_http_info(self, model, id, **kwargs):  # noqa: E501
        """Updates the models currently in db.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.trello_model_id_put_with_http_info(model, id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str model: (required)
        :param str id: (required)
        :return: UniversalResource
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['model', 'id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method trello_model_id_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'model' is set
        if ('model' not in params or
                params['model'] is None):
            raise ValueError("Missing the required parameter `model` when calling `trello_model_id_put`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `trello_model_id_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'model' in params:
            path_params['model'] = params['model']  # noqa: E501
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/trello/{model}/{id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UniversalResource',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def trello_post(self, **kwargs):  # noqa: E501
        """trello_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.trello_post(async=True)
        >>> result = thread.get()

        :param async bool
        :param str key:
        :param str token:
        :param TrelloQuery query:
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.trello_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.trello_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def trello_post_with_http_info(self, **kwargs):  # noqa: E501
        """trello_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.trello_post_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str key:
        :param str token:
        :param TrelloQuery query:
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['key', 'token', 'query']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method trello_post" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'key' in params:
            query_params.append(('key', params['key']))  # noqa: E501
        if 'token' in params:
            query_params.append(('token', params['token']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'query' in params:
            body_params = params['query']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/trello/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='int',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def trello_put(self, **kwargs):  # noqa: E501
        """trello_put  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.trello_put(async=True)
        >>> result = thread.get()

        :param async bool
        :param str key:
        :param str token:
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.trello_put_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.trello_put_with_http_info(**kwargs)  # noqa: E501
            return data

    def trello_put_with_http_info(self, **kwargs):  # noqa: E501
        """trello_put  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.trello_put_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str key:
        :param str token:
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['key', 'token']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method trello_put" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'key' in params:
            query_params.append(('key', params['key']))  # noqa: E501
        if 'token' in params:
            query_params.append(('token', params['token']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/trello/', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='int',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
