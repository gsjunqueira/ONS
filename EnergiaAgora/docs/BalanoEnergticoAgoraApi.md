# swagger_client.BalanoEnergticoAgoraApi

All URIs are relative to *https://integra.ons.org.br/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_balanco_energetico**](BalanoEnergticoAgoraApi.md#get_balanco_energetico) | **GET** /energiaagora/GetBalancoEnergetico/null | 

# **get_balanco_energetico**
> BalancoEnergetico get_balanco_energetico()



Obter a o balanço energético (MW) em tempo real

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.BalanoEnergticoAgoraApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_balanco_energetico()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BalanoEnergticoAgoraApi->get_balanco_energetico: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**BalancoEnergetico**](BalancoEnergetico.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

