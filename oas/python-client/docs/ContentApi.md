# jatdb_client.ContentApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**content_get**](ContentApi.md#content_get) | **GET** /content/ | 
[**content_post**](ContentApi.md#content_post) | **POST** /content/ | 
[**content_put**](ContentApi.md#content_put) | **PUT** /content/ | 


# **content_get**
> ContentFile content_get(path)



### Example
```python
from __future__ import print_function
import time
import jatdb_client
from jatdb_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jatdb_client.ContentApi()
path = 'path_example' # str | Relative path to file

try:
    api_response = api_instance.content_get(path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentApi->content_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Relative path to file | 

### Return type

[**ContentFile**](ContentFile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **content_post**
> UniversalResource content_post(contentfile)



### Example
```python
from __future__ import print_function
import time
import jatdb_client
from jatdb_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jatdb_client.ContentApi()
contentfile = jatdb_client.ContentFile() # ContentFile | 

try:
    api_response = api_instance.content_post(contentfile)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentApi->content_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contentfile** | [**ContentFile**](ContentFile.md)|  | 

### Return type

[**UniversalResource**](UniversalResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **content_put**
> UniversalResource content_put(path, contentfile)



### Example
```python
from __future__ import print_function
import time
import jatdb_client
from jatdb_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jatdb_client.ContentApi()
path = 'path_example' # str | Relative path to file
contentfile = jatdb_client.ContentFile() # ContentFile | 

try:
    api_response = api_instance.content_put(path, contentfile)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentApi->content_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Relative path to file | 
 **contentfile** | [**ContentFile**](ContentFile.md)|  | 

### Return type

[**UniversalResource**](UniversalResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

