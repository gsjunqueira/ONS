# swagger_client.GrandezasPrevistasApi

All URIs are relative to *https://integra.ons.org.br/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**consultar_previsoes**](GrandezasPrevistasApi.md#consultar_previsoes) | **GET** /hidrologia/previsoes/{reservatorio}/vazao-diaria | Realiza a consulta das previsões das vazões diárias por reservatório.

# **consultar_previsoes**
> ResultadoPrevisaoReservatorio consultar_previsoes(reservatorio, data_inicio_previsao, data_validade_previsao, pagina=pagina, quantidade=quantidade)

Realiza a consulta das previsões das vazões diárias por reservatório.

Realiza a consulta das previsões das vazões diárias por reservatório.

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
api_instance = swagger_client.GrandezasPrevistasApi(swagger_client.ApiClient(configuration))
reservatorio = 'reservatorio_example' # str | identificador do reservatório.
data_inicio_previsao = '2013-10-20T19:20:30+01:00' # datetime | data de início da previsão  (AAAA-MM-DD).
data_validade_previsao = ['2013-10-20'] # list[date] | datas de validade da previsão (AAAA-MM-DD).
pagina = 56 # int | página para recuperação das previsões. (optional)
quantidade = 56 # int | quantidade por página. (optional)

try:
    # Realiza a consulta das previsões das vazões diárias por reservatório.
    api_response = api_instance.consultar_previsoes(reservatorio, data_inicio_previsao, data_validade_previsao, pagina=pagina, quantidade=quantidade)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GrandezasPrevistasApi->consultar_previsoes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reservatorio** | **str**| identificador do reservatório. | 
 **data_inicio_previsao** | **datetime**| data de início da previsão  (AAAA-MM-DD). | 
 **data_validade_previsao** | [**list[date]**](date.md)| datas de validade da previsão (AAAA-MM-DD). | 
 **pagina** | **int**| página para recuperação das previsões. | [optional] 
 **quantidade** | **int**| quantidade por página. | [optional] 

### Return type

[**ResultadoPrevisaoReservatorio**](ResultadoPrevisaoReservatorio.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

