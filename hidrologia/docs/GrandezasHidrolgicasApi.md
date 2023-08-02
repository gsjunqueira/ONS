# swagger_client.GrandezasHidrolgicasApi

All URIs are relative to *https://integra.ons.org.br/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_grandezas_hidrologicas**](GrandezasHidrolgicasApi.md#get_grandezas_hidrologicas) | **GET** /hidrologia/GrandezasHidrologicas | 

# **get_grandezas_hidrologicas**
> GrandezasHidrologicasResult get_grandezas_hidrologicas(pagina, quantidade, id_posto_reservatorio, grandeza, data_inicial_medicao, data_final_medicao, qualidade_dado, agregacao_temporal)



Obter lista de grandezas hidrológicas

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
api_instance = swagger_client.GrandezasHidrolgicasApi(swagger_client.ApiClient(configuration))
pagina = 0 # int | Página corrente (default to 0)
quantidade = 10 # int | Quantidade de resultados por página (default to 10)
id_posto_reservatorio = ['id_posto_reservatorio_example'] # list[str] | Lista de IDs dos Postos ou Reservatórios, é necessário informar no mínimo um ID
grandeza = ['grandeza_example'] # list[str] | Informar apenas uma das Grandezas <li>VMD - Vazão média do posto fluviométrico <li>AFL - Afluência de Reservatório <li>DFL - Descarga média total de Reservatório <li>TUR - Vazão turbinada <li>VER - Vazão Média Vertida de Reservatório <li>VTR - Indicador de Energia Turbinável por Região <li>VOE - Vazão de Outras estruturas <li>NIV - Nível de Reservatório as 24h <li>NIS - Geração Nuclear Instantânea do Sistema Interligado <li>VNA - Vazão Natural Total <li>VNM - Vazão Natural Incrementalde Mádia Móvel <li>VNS - Vazão Incremental da sub-bacia modelada. Vazão utilizada nos modelos de previsão, considerando os postos fluviométricos <li>VIA - Vazão incremental agrupada. VAzão incremental entre dois reservatórios, considerando a existência de outro(s) reservatório(s) no trecho incremental
data_inicial_medicao = '2013-10-20' # date | Data inicial do período de Medição no formato dd/mm/aaaa
data_final_medicao = '2013-10-20' # date | Data final do período de Medição no formato dd/mm/aaaa
qualidade_dado = ['qualidade_dado_example'] # list[str] | Informar a Qualidade do Dado, se deseja dados Consistidos (COO) e/ou Consolidados (CON).
agregacao_temporal = ['agregacao_temporal_example'] # list[str] | Informar a Agregação Temporal, se deseja Diária ou Horária.

try:
    api_response = api_instance.get_grandezas_hidrologicas(pagina, quantidade, id_posto_reservatorio, grandeza, data_inicial_medicao, data_final_medicao, qualidade_dado, agregacao_temporal)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GrandezasHidrolgicasApi->get_grandezas_hidrologicas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pagina** | **int**| Página corrente | [default to 0]
 **quantidade** | **int**| Quantidade de resultados por página | [default to 10]
 **id_posto_reservatorio** | [**list[str]**](str.md)| Lista de IDs dos Postos ou Reservatórios, é necessário informar no mínimo um ID | 
 **grandeza** | [**list[str]**](str.md)| Informar apenas uma das Grandezas &lt;li&gt;VMD - Vazão média do posto fluviométrico &lt;li&gt;AFL - Afluência de Reservatório &lt;li&gt;DFL - Descarga média total de Reservatório &lt;li&gt;TUR - Vazão turbinada &lt;li&gt;VER - Vazão Média Vertida de Reservatório &lt;li&gt;VTR - Indicador de Energia Turbinável por Região &lt;li&gt;VOE - Vazão de Outras estruturas &lt;li&gt;NIV - Nível de Reservatório as 24h &lt;li&gt;NIS - Geração Nuclear Instantânea do Sistema Interligado &lt;li&gt;VNA - Vazão Natural Total &lt;li&gt;VNM - Vazão Natural Incrementalde Mádia Móvel &lt;li&gt;VNS - Vazão Incremental da sub-bacia modelada. Vazão utilizada nos modelos de previsão, considerando os postos fluviométricos &lt;li&gt;VIA - Vazão incremental agrupada. VAzão incremental entre dois reservatórios, considerando a existência de outro(s) reservatório(s) no trecho incremental | 
 **data_inicial_medicao** | **date**| Data inicial do período de Medição no formato dd/mm/aaaa | 
 **data_final_medicao** | **date**| Data final do período de Medição no formato dd/mm/aaaa | 
 **qualidade_dado** | [**list[str]**](str.md)| Informar a Qualidade do Dado, se deseja dados Consistidos (COO) e/ou Consolidados (CON). | 
 **agregacao_temporal** | [**list[str]**](str.md)| Informar a Agregação Temporal, se deseja Diária ou Horária. | 

### Return type

[**GrandezasHidrologicasResult**](GrandezasHidrologicasResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

