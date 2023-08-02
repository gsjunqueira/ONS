# swagger_client.CargaMinutoAMinutoHojeApi

All URIs are relative to *https://integra.ons.org.br/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**gett_consultar_carga_minuto**](CargaMinutoAMinutoHojeApi.md#gett_consultar_carga_minuto) | **GET** /energiaagora/Get/{cargasubsistema} | 

# **gett_consultar_carga_minuto**
> CargaMinuto gett_consultar_carga_minuto(cargasubsistema)



Carga do dia minuto a minuto em MW

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
api_instance = swagger_client.CargaMinutoAMinutoHojeApi(swagger_client.ApiClient(configuration))
cargasubsistema = 'cargasubsistema_example' # str | 

try:
    api_response = api_instance.gett_consultar_carga_minuto(cargasubsistema)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CargaMinutoAMinutoHojeApi->gett_consultar_carga_minuto: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cargasubsistema** | **str**|  | 

### Return type

[**CargaMinuto**](CargaMinuto.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

