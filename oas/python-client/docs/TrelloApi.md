# jatdb_client.TrelloApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**trello_model_id_put**](TrelloApi.md#trello_model_id_put) | **PUT** /trello/{model}/{id} | Updates the models currently in db.
[**trello_post**](TrelloApi.md#trello_post) | **POST** /trello/ | 
[**trello_put**](TrelloApi.md#trello_put) | **PUT** /trello/ | 


# **trello_model_id_put**
> UniversalResource trello_model_id_put(model, id)

Updates the models currently in db.

### Example
```python
from __future__ import print_function
import time
import jatdb_client
from jatdb_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jatdb_client.TrelloApi()
model = 'model_example' # str | 
id = 'id_example' # str | 

try:
    # Updates the models currently in db.
    api_response = api_instance.trello_model_id_put(model, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrelloApi->trello_model_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**UniversalResource**](UniversalResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trello_post**
> int trello_post(key=key, token=token, query=query)



### Example
```python
from __future__ import print_function
import time
import jatdb_client
from jatdb_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jatdb_client.TrelloApi()
key = 'key_example' # str |  (optional)
token = 'token_example' # str |  (optional)
query = jatdb_client.TrelloQuery() # TrelloQuery |  (optional)

try:
    api_response = api_instance.trello_post(key=key, token=token, query=query)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrelloApi->trello_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**|  | [optional] 
 **token** | **str**|  | [optional] 
 **query** | [**TrelloQuery**](TrelloQuery.md)|  | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trello_put**
> int trello_put(key=key, token=token)



### Example
```python
from __future__ import print_function
import time
import jatdb_client
from jatdb_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jatdb_client.TrelloApi()
key = 'key_example' # str |  (optional)
token = 'token_example' # str |  (optional)

try:
    api_response = api_instance.trello_put(key=key, token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrelloApi->trello_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**|  | [optional] 
 **token** | **str**|  | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

