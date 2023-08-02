# swagger_client.UsinaApi

All URIs are relative to *https://integra.ons.org.br/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**insumo_pdp_listar_geracao_proposta**](UsinaApi.md#insumo_pdp_listar_geracao_proposta) | **POST** /programacao/usina/ListarGeracaoProposta | Listar a geração proposta por Usina em base semi-horária.
[**insumo_pdp_listar_geracao_proposta_get**](UsinaApi.md#insumo_pdp_listar_geracao_proposta_get) | **GET** /programacao/usina/ListarGeracaoPropostaGET | Listar a geração proposta por Usina em base semi-horária.
[**insumo_pdp_listar_usinas_representadas**](UsinaApi.md#insumo_pdp_listar_usinas_representadas) | **GET** /programacao/usina/ListarUsinasRepresentadas | Listar Usinas representadas pelo usuário.

# **insumo_pdp_listar_geracao_proposta**
> GeracaoPropostaResponse insumo_pdp_listar_geracao_proposta(body)

Listar a geração proposta por Usina em base semi-horária.

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
api_instance = swagger_client.UsinaApi(swagger_client.ApiClient(configuration))
body = swagger_client.GeracaoPropostaRequest() # GeracaoPropostaRequest | Parâmetros de requisição

try:
    # Listar a geração proposta por Usina em base semi-horária.
    api_response = api_instance.insumo_pdp_listar_geracao_proposta(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsinaApi->insumo_pdp_listar_geracao_proposta: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GeracaoPropostaRequest**](GeracaoPropostaRequest.md)| Parâmetros de requisição | 

### Return type

[**GeracaoPropostaResponse**](GeracaoPropostaResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insumo_pdp_listar_geracao_proposta_get**
> GeracaoPropostaGETResponse insumo_pdp_listar_geracao_proposta_get(request_ano, request_mes, request_dia, request_numero_paginacao, request_quantidade_pagina, request_codigos_usinas=request_codigos_usinas)

Listar a geração proposta por Usina em base semi-horária.

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
api_instance = swagger_client.UsinaApi(swagger_client.ApiClient(configuration))
request_ano = 56 # int | (Obrigatório) Data do PDP (Ano).
request_mes = 56 # int | (Obrigatório) Data do PDP (Mês).
request_dia = 56 # int | (Obrigatório) Data do PDP (Dia).
request_numero_paginacao = 56 # int | (Obrigatório) Paginação: Número da página.
request_quantidade_pagina = 56 # int | 
request_codigos_usinas = ['request_codigos_usinas_example'] # list[str] | (Opcional) Código das Usinas no PDP (Caso não informado retornará a geração de todos as usinas relacionadas ao usuário) (optional)

try:
    # Listar a geração proposta por Usina em base semi-horária.
    api_response = api_instance.insumo_pdp_listar_geracao_proposta_get(request_ano, request_mes, request_dia, request_numero_paginacao, request_quantidade_pagina, request_codigos_usinas=request_codigos_usinas)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsinaApi->insumo_pdp_listar_geracao_proposta_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_ano** | **int**| (Obrigatório) Data do PDP (Ano). | 
 **request_mes** | **int**| (Obrigatório) Data do PDP (Mês). | 
 **request_dia** | **int**| (Obrigatório) Data do PDP (Dia). | 
 **request_numero_paginacao** | **int**| (Obrigatório) Paginação: Número da página. | 
 **request_quantidade_pagina** | **int**|  | 
 **request_codigos_usinas** | [**list[str]**](str.md)| (Opcional) Código das Usinas no PDP (Caso não informado retornará a geração de todos as usinas relacionadas ao usuário) | [optional] 

### Return type

[**GeracaoPropostaGETResponse**](GeracaoPropostaGETResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insumo_pdp_listar_usinas_representadas**
> UsinaResponse insumo_pdp_listar_usinas_representadas(request_codigos_empresas=request_codigos_empresas)

Listar Usinas representadas pelo usuário.

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
api_instance = swagger_client.UsinaApi(swagger_client.ApiClient(configuration))
request_codigos_empresas = ['request_codigos_empresas_example'] # list[str] | (Opcional) Código das Empresas no PDP (Caso não informado retornará todos as usinas relacionadas ao usuário) (optional)

try:
    # Listar Usinas representadas pelo usuário.
    api_response = api_instance.insumo_pdp_listar_usinas_representadas(request_codigos_empresas=request_codigos_empresas)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsinaApi->insumo_pdp_listar_usinas_representadas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_codigos_empresas** | [**list[str]**](str.md)| (Opcional) Código das Empresas no PDP (Caso não informado retornará todos as usinas relacionadas ao usuário) | [optional] 

### Return type

[**UsinaResponse**](UsinaResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

