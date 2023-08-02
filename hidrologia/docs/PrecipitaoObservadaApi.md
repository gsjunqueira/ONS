# swagger_client.PrecipitaoObservadaApi

All URIs are relative to *https://integra.ons.org.br/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_precipitacao_observada**](PrecipitaoObservadaApi.md#get_precipitacao_observada) | **GET** /hidrologia/PrecipitacaoObservada | 

# **get_precipitacao_observada**
> PrecipacaoObservadaResult get_precipitacao_observada(pagina, quantidade, id_estacao_meteo, data_inicial_medicao, data_final_medicao, qualidade_dado, agregacao_temporal, furo_temporal)



Obter lista de precipitações observadas

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
api_instance = swagger_client.PrecipitaoObservadaApi(swagger_client.ApiClient(configuration))
pagina = 0 # int | Página corrente (default to 0)
quantidade = 10 # int | Quantidade de resultados por página (default to 10)
id_estacao_meteo = 'id_estacao_meteo_example' # str | Lista de IDs das Estações Meteorológica, é necessário informar no mínimo um ID
data_inicial_medicao = '2013-10-20' # date | Data inicial do período de Medição no formato dd/mm/aaaa
data_final_medicao = '2013-10-20' # date | Data final do período de Medição no formato dd/mm/aaaa
qualidade_dado = ['qualidade_dado_example'] # list[str] | Informar a Qualidade do Dado, se deseja dados Consistidos e/ou Consolidados.
agregacao_temporal = ['agregacao_temporal_example'] # list[str] | Informar a Agregação Temporal, se deseja Diária ou Horária.
furo_temporal = ['furo_temporal_example'] # list[str] | Informar se deseja retornar Furo Temporal.

try:
    api_response = api_instance.get_precipitacao_observada(pagina, quantidade, id_estacao_meteo, data_inicial_medicao, data_final_medicao, qualidade_dado, agregacao_temporal, furo_temporal)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrecipitaoObservadaApi->get_precipitacao_observada: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pagina** | **int**| Página corrente | [default to 0]
 **quantidade** | **int**| Quantidade de resultados por página | [default to 10]
 **id_estacao_meteo** | **str**| Lista de IDs das Estações Meteorológica, é necessário informar no mínimo um ID | 
 **data_inicial_medicao** | **date**| Data inicial do período de Medição no formato dd/mm/aaaa | 
 **data_final_medicao** | **date**| Data final do período de Medição no formato dd/mm/aaaa | 
 **qualidade_dado** | [**list[str]**](str.md)| Informar a Qualidade do Dado, se deseja dados Consistidos e/ou Consolidados. | 
 **agregacao_temporal** | [**list[str]**](str.md)| Informar a Agregação Temporal, se deseja Diária ou Horária. | 
 **furo_temporal** | [**list[str]**](str.md)| Informar se deseja retornar Furo Temporal. | 

### Return type

[**PrecipacaoObservadaResult**](PrecipacaoObservadaResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

