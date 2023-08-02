# swagger_client.GeraoPorFonteMinutoAMinutoHojeApi

All URIs are relative to *https://integra.ons.org.br/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_consultar_gearacai_mminuto**](GeraoPorFonteMinutoAMinutoHojeApi.md#get_consultar_gearacai_mminuto) | **GET** /energiaagora/Get/{geracaosubsistema} | 

# **get_consultar_gearacai_mminuto**
> GeracaoMinuto get_consultar_gearacai_mminuto(geracaosubsistema)



Geração do dia minuto a minuto em MW

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
api_instance = swagger_client.GeraoPorFonteMinutoAMinutoHojeApi(swagger_client.ApiClient(configuration))
geracaosubsistema = 'geracaosubsistema_example' # str | 

try:
    api_response = api_instance.get_consultar_gearacai_mminuto(geracaosubsistema)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeraoPorFonteMinutoAMinutoHojeApi->get_consultar_gearacai_mminuto: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **geracaosubsistema** | **str**|  | 

### Return type

[**GeracaoMinuto**](GeracaoMinuto.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

