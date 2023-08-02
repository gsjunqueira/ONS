# swagger_client.BalancoProgramadoApi

All URIs are relative to *https://integra.ons.org.br/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**balanco_programado_listar_carga_medio_diaria**](BalancoProgramadoApi.md#balanco_programado_listar_carga_medio_diaria) | **GET** /programacao/repdoe/CargaMedioDiario | Listar a carga do balanço programado de energia médio diário (MWMED) por Região
[**balanco_programado_listar_geracao_medio_diaria**](BalancoProgramadoApi.md#balanco_programado_listar_geracao_medio_diaria) | **POST** /programacao/repdoe/GeracaoMedioDiario | Listar a geração do balanço programado de energia médio diário (MWMED) por Região
[**balanco_programado_listar_intercambio_liquido_medio_diaria**](BalancoProgramadoApi.md#balanco_programado_listar_intercambio_liquido_medio_diaria) | **GET** /programacao/repdoe/IntercambioLiquidoMedioDiario | Listar o intercâmbio liquido programado por Região

# **balanco_programado_listar_carga_medio_diaria**
> BalancoCargaResponse balanco_programado_listar_carga_medio_diaria(ano, mes, dia)

Listar a carga do balanço programado de energia médio diário (MWMED) por Região

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
api_instance = swagger_client.BalancoProgramadoApi(swagger_client.ApiClient(configuration))
ano = 56 # int | (Obrigatório) Data do PDP (Ano).
mes = 56 # int | (Obrigatório) Data do PDP (Mes).
dia = 56 # int | (Obrigatório) Data do PDP (Dia).

try:
    # Listar a carga do balanço programado de energia médio diário (MWMED) por Região
    api_response = api_instance.balanco_programado_listar_carga_medio_diaria(ano, mes, dia)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BalancoProgramadoApi->balanco_programado_listar_carga_medio_diaria: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ano** | **int**| (Obrigatório) Data do PDP (Ano). | 
 **mes** | **int**| (Obrigatório) Data do PDP (Mes). | 
 **dia** | **int**| (Obrigatório) Data do PDP (Dia). | 

### Return type

[**BalancoCargaResponse**](BalancoCargaResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **balanco_programado_listar_geracao_medio_diaria**
> BalancoGeracaoResponse balanco_programado_listar_geracao_medio_diaria(body)

Listar a geração do balanço programado de energia médio diário (MWMED) por Região

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
api_instance = swagger_client.BalancoProgramadoApi(swagger_client.ApiClient(configuration))
body = swagger_client.BalancoRequest() # BalancoRequest | Parâmetros de requisição

try:
    # Listar a geração do balanço programado de energia médio diário (MWMED) por Região
    api_response = api_instance.balanco_programado_listar_geracao_medio_diaria(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BalancoProgramadoApi->balanco_programado_listar_geracao_medio_diaria: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BalancoRequest**](BalancoRequest.md)| Parâmetros de requisição | 

### Return type

[**BalancoGeracaoResponse**](BalancoGeracaoResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **balanco_programado_listar_intercambio_liquido_medio_diaria**
> BalancoIntercambioLiquidoResponse balanco_programado_listar_intercambio_liquido_medio_diaria(ano, mes, dia)

Listar o intercâmbio liquido programado por Região

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
api_instance = swagger_client.BalancoProgramadoApi(swagger_client.ApiClient(configuration))
ano = 56 # int | (Obrigatório) Data do PDP (Ano).
mes = 56 # int | (Obrigatório) Data do PDP (Mes).
dia = 56 # int | (Obrigatório) Data do PDP (Dia).

try:
    # Listar o intercâmbio liquido programado por Região
    api_response = api_instance.balanco_programado_listar_intercambio_liquido_medio_diaria(ano, mes, dia)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BalancoProgramadoApi->balanco_programado_listar_intercambio_liquido_medio_diaria: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ano** | **int**| (Obrigatório) Data do PDP (Ano). | 
 **mes** | **int**| (Obrigatório) Data do PDP (Mes). | 
 **dia** | **int**| (Obrigatório) Data do PDP (Dia). | 

### Return type

[**BalancoIntercambioLiquidoResponse**](BalancoIntercambioLiquidoResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

