# jatdb_client.DefaultApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**uri_post**](DefaultApi.md#uri_post) | **POST** /uri/ | 


# **uri_post**
> UniversalResource uri_post(uri)



### Example
```python
from __future__ import print_function
import time
import jatdb_client
from jatdb_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jatdb_client.DefaultApi()
uri = jatdb_client.UniversalResource() # UniversalResource | 

try:
    api_response = api_instance.uri_post(uri)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->uri_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | [**UniversalResource**](UniversalResource.md)|  | 

### Return type

[**UniversalResource**](UniversalResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

