# swagger_client.ReservatrioApi

All URIs are relative to *https://integra.ons.org.br/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_reservatorios**](ReservatrioApi.md#get_reservatorios) | **GET** /hidrologia/reservatorios | 
[**get_reservatorios_by_id**](ReservatrioApi.md#get_reservatorios_by_id) | **GET** /hidrologia/reservatorios/{Identificador} | 

# **get_reservatorios**
> ResultadoConsultaReservatoriosPaginada get_reservatorios(pagina, quantidade)



Obter a lista de reservatorios

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
api_instance = swagger_client.ReservatrioApi(swagger_client.ApiClient(configuration))
pagina = 1 # int | Pagina corrente (default to 1)
quantidade = 240 # int | Quantidade de resultados por pagina (default to 240)

try:
    api_response = api_instance.get_reservatorios(pagina, quantidade)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReservatrioApi->get_reservatorios: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pagina** | **int**| Pagina corrente | [default to 1]
 **quantidade** | **int**| Quantidade de resultados por pagina | [default to 240]

### Return type

[**ResultadoConsultaReservatoriosPaginada**](ResultadoConsultaReservatoriosPaginada.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reservatorios_by_id**
> Reservatorio get_reservatorios_by_id(identificador)



Obter as informacoes detalhadas de um reservatorio

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
api_instance = swagger_client.ReservatrioApi(swagger_client.ApiClient(configuration))
identificador = 'identificador_example' # str | Identificador do Reservatorio

try:
    api_response = api_instance.get_reservatorios_by_id(identificador)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReservatrioApi->get_reservatorios_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identificador** | **str**| Identificador do Reservatorio | 

### Return type

[**Reservatorio**](Reservatorio.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

