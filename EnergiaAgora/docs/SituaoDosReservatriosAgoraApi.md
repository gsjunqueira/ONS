# swagger_client.SituaoDosReservatriosAgoraApi

All URIs are relative to *https://integra.ons.org.br/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**situacao_dos_reservatorios**](SituaoDosReservatriosAgoraApi.md#situacao_dos_reservatorios) | **GET** /energiaagora/Get/SituacaoDosReservatorios | 

# **situacao_dos_reservatorios**
> SituacaoReservatorio situacao_dos_reservatorios()



Obter a lista da situação dos reservatórios em tempo real

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
api_instance = swagger_client.SituaoDosReservatriosAgoraApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.situacao_dos_reservatorios()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SituaoDosReservatriosAgoraApi->situacao_dos_reservatorios: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SituacaoReservatorio**](SituacaoReservatorio.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

