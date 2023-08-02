# swagger_client.IntervencaoControllerApi

All URIs are relative to *https://integra.ons.org.br/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**consultar_dados_dominios_intervencao**](IntervencaoControllerApi.md#consultar_dados_dominios_intervencao) | **GET** /sgi/dominios/{tipo} | Realiza a obtenção dos domínios em função do tipo recebido.
[**consultar_historico_dados_execucao**](IntervencaoControllerApi.md#consultar_historico_dados_execucao) | **GET** /sgi/intervencoes/historico-execucao/{identificadorONS} | Realiza a obtenção do historico e dados de execução da intervenção com base no Identificador ONS informado
[**consultar_intervencoes_sgi**](IntervencaoControllerApi.md#consultar_intervencoes_sgi) | **GET** /sgi/intervencoes | Realiza a obtenção das intervenções com base no filtro recebido.
[**consultar_situacao_importacao_lote**](IntervencaoControllerApi.md#consultar_situacao_importacao_lote) | **GET** /sgi/intervencoes/importar-lote/{id} | Realiza a obtenção da situação de um lote de importação de intervençoes.
[**upload_lote_intervencoes**](IntervencaoControllerApi.md#upload_lote_intervencoes) | **POST** /sgi/intervencoes/importar-lote | Realiza o processo de upload dos arquivos para criação das intervenções em lote.

# **consultar_dados_dominios_intervencao**
> RespostaConsultaDominiosDto consultar_dados_dominios_intervencao(tipo)

Realiza a obtenção dos domínios em função do tipo recebido.

Realiza a obtenção dos domínios em função do tipo recebido. Os tipos de domínios são utilizados como filtro da API de intervenções (/sgi/intervencoes): <li>1 - AGENTES <li>2 - UF <li>3 - ESTADO_ATUAL <li>4 - CENTRO_RESPONSAVEL <li>5 - MALHA <li>6 - TIPO <li>7 - CARACTERIZACAO <li>8 - NATUREZA

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
api_instance = swagger_client.IntervencaoControllerApi(swagger_client.ApiClient(configuration))
tipo = 56 # int | tipo domímino a ser recuperado.

try:
    # Realiza a obtenção dos domínios em função do tipo recebido.
    api_response = api_instance.consultar_dados_dominios_intervencao(tipo)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntervencaoControllerApi->consultar_dados_dominios_intervencao: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tipo** | **int**| tipo domímino a ser recuperado. | 

### Return type

[**RespostaConsultaDominiosDto**](RespostaConsultaDominiosDto.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **consultar_historico_dados_execucao**
> ResultadoHistoricoDadosExecucaoIntervencaoDto consultar_historico_dados_execucao(identificador_ons)

Realiza a obtenção do historico e dados de execução da intervenção com base no Identificador ONS informado

Realiza a obtenção do historico e dados de execução da intervenção com base no Identificador ONS informado

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
api_instance = swagger_client.IntervencaoControllerApi(swagger_client.ApiClient(configuration))
identificador_ons = 'identificador_ons_example' # str | Identificador ONS informado a ser informado.

try:
    # Realiza a obtenção do historico e dados de execução da intervenção com base no Identificador ONS informado
    api_response = api_instance.consultar_historico_dados_execucao(identificador_ons)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntervencaoControllerApi->consultar_historico_dados_execucao: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identificador_ons** | **str**| Identificador ONS informado a ser informado. | 

### Return type

[**ResultadoHistoricoDadosExecucaoIntervencaoDto**](ResultadoHistoricoDadosExecucaoIntervencaoDto.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **consultar_intervencoes_sgi**
> RespostaConsultaIntervencaoDto consultar_intervencoes_sgi(filtro_numero_ons=filtro_numero_ons, filtro_numero_agente=filtro_numero_agente, filtro_data_inicio=filtro_data_inicio, filtro_data_fim=filtro_data_fim, filtro_agentes_solicitantes=filtro_agentes_solicitantes, filtro_u_fs=filtro_u_fs, filtro_situacoes=filtro_situacoes, filtro_centro_responsavel=filtro_centro_responsavel, filtro_malha=filtro_malha, filtro_tipo=filtro_tipo, filtro_caracterizacao=filtro_caracterizacao, filtro_natureza=filtro_natureza)

Realiza a obtenção das intervenções com base no filtro recebido.

Realiza a obtenção das intervenções com base no filtro recebido.

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
api_instance = swagger_client.IntervencaoControllerApi(swagger_client.ApiClient(configuration))
filtro_numero_ons = 'filtro_numero_ons_example' # str | Número da intervenção no ONS. (optional)
filtro_numero_agente = 'filtro_numero_agente_example' # str | Número do agente. (optional)
filtro_data_inicio = '2013-10-20T19:20:30+01:00' # datetime | Data de Início  no formato yyyy-mm-dd'. (optional)
filtro_data_fim = '2013-10-20T19:20:30+01:00' # datetime | Data fim  no formato yyyy-mm-dd'. (optional)
filtro_agentes_solicitantes = ['filtro_agentes_solicitantes_example'] # list[str] | Listagem com os agentes solicitantes. A lista de agentes pode ser obtida em /sgi/dominios/{tipo} (Tipo 1). (optional)
filtro_u_fs = ['filtro_u_fs_example'] # list[str] | Listagem com as unidades federativas. A lista de UFs pode ser obtida em /sgi/dominios/{tipo} (Tipo 2). (optional)
filtro_situacoes = [56] # list[int] | Lista com as situacoes. A lista de Situações pode ser obtida em /sgi/dominios/{tipo} (Tipo 3). (optional)
filtro_centro_responsavel = 'filtro_centro_responsavel_example' # str | Centro responsável. A lista dos Centros pode ser obtida em /sgi/dominios/{tipo} (Tipo 4). (optional)
filtro_malha = 56 # int | Malha da intervenção. A lista de Malhas pode ser obtida em /sgi/dominios/{tipo} (Tipo 5). (optional)
filtro_tipo = 56 # int | Tipo da intervenção. A lista de Tipos pode ser obtida em /sgi/dominios/{tipo} (Tipo 6). (optional)
filtro_caracterizacao = 56 # int | Caracterização da intervenção. A lista de Caracterizações pode ser obtida em /sgi/dominios/{tipo} (Tipo 7). (optional)
filtro_natureza = 56 # int | Natureza da intervenção. A lista de Naturezas pode ser obtida em /sgi/dominios/{tipo} (Tipo 8). (optional)

try:
    # Realiza a obtenção das intervenções com base no filtro recebido.
    api_response = api_instance.consultar_intervencoes_sgi(filtro_numero_ons=filtro_numero_ons, filtro_numero_agente=filtro_numero_agente, filtro_data_inicio=filtro_data_inicio, filtro_data_fim=filtro_data_fim, filtro_agentes_solicitantes=filtro_agentes_solicitantes, filtro_u_fs=filtro_u_fs, filtro_situacoes=filtro_situacoes, filtro_centro_responsavel=filtro_centro_responsavel, filtro_malha=filtro_malha, filtro_tipo=filtro_tipo, filtro_caracterizacao=filtro_caracterizacao, filtro_natureza=filtro_natureza)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntervencaoControllerApi->consultar_intervencoes_sgi: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filtro_numero_ons** | **str**| Número da intervenção no ONS. | [optional] 
 **filtro_numero_agente** | **str**| Número do agente. | [optional] 
 **filtro_data_inicio** | **datetime**| Data de Início  no formato yyyy-mm-dd&#x27;. | [optional] 
 **filtro_data_fim** | **datetime**| Data fim  no formato yyyy-mm-dd&#x27;. | [optional] 
 **filtro_agentes_solicitantes** | [**list[str]**](str.md)| Listagem com os agentes solicitantes. A lista de agentes pode ser obtida em /sgi/dominios/{tipo} (Tipo 1). | [optional] 
 **filtro_u_fs** | [**list[str]**](str.md)| Listagem com as unidades federativas. A lista de UFs pode ser obtida em /sgi/dominios/{tipo} (Tipo 2). | [optional] 
 **filtro_situacoes** | [**list[int]**](int.md)| Lista com as situacoes. A lista de Situações pode ser obtida em /sgi/dominios/{tipo} (Tipo 3). | [optional] 
 **filtro_centro_responsavel** | **str**| Centro responsável. A lista dos Centros pode ser obtida em /sgi/dominios/{tipo} (Tipo 4). | [optional] 
 **filtro_malha** | **int**| Malha da intervenção. A lista de Malhas pode ser obtida em /sgi/dominios/{tipo} (Tipo 5). | [optional] 
 **filtro_tipo** | **int**| Tipo da intervenção. A lista de Tipos pode ser obtida em /sgi/dominios/{tipo} (Tipo 6). | [optional] 
 **filtro_caracterizacao** | **int**| Caracterização da intervenção. A lista de Caracterizações pode ser obtida em /sgi/dominios/{tipo} (Tipo 7). | [optional] 
 **filtro_natureza** | **int**| Natureza da intervenção. A lista de Naturezas pode ser obtida em /sgi/dominios/{tipo} (Tipo 8). | [optional] 

### Return type

[**RespostaConsultaIntervencaoDto**](RespostaConsultaIntervencaoDto.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **consultar_situacao_importacao_lote**
> RespostaConsultaSituacaoImportacaoLoteDto consultar_situacao_importacao_lote(id)

Realiza a obtenção da situação de um lote de importação de intervençoes.

Realiza a obtenção da situação de um lote de importação de intervençoes.

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
api_instance = swagger_client.IntervencaoControllerApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | identificador do lote a ser verificado.

try:
    # Realiza a obtenção da situação de um lote de importação de intervençoes.
    api_response = api_instance.consultar_situacao_importacao_lote(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntervencaoControllerApi->consultar_situacao_importacao_lote: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identificador do lote a ser verificado. | 

### Return type

[**RespostaConsultaSituacaoImportacaoLoteDto**](RespostaConsultaSituacaoImportacaoLoteDto.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_lote_intervencoes**
> RespostaUploadIntervencoesDto upload_lote_intervencoes(anexo9, anexo10, anexo2, arquivo_dados, anexo8, anexo4, anexo5, anexo3, anexo6, anexo7, anexo1)

Realiza o processo de upload dos arquivos para criação das intervenções em lote.

Realiza o processo de upload dos arquivos para criação das intervenções em lote.

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
api_instance = swagger_client.IntervencaoControllerApi(swagger_client.ApiClient(configuration))
anexo9 = 'anexo9_example' # str | 
anexo10 = 'anexo10_example' # str | 
anexo2 = 'anexo2_example' # str | 
arquivo_dados = 'arquivo_dados_example' # str | 
anexo8 = 'anexo8_example' # str | 
anexo4 = 'anexo4_example' # str | 
anexo5 = 'anexo5_example' # str | 
anexo3 = 'anexo3_example' # str | 
anexo6 = 'anexo6_example' # str | 
anexo7 = 'anexo7_example' # str | 
anexo1 = 'anexo1_example' # str | 

try:
    # Realiza o processo de upload dos arquivos para criação das intervenções em lote.
    api_response = api_instance.upload_lote_intervencoes(anexo9, anexo10, anexo2, arquivo_dados, anexo8, anexo4, anexo5, anexo3, anexo6, anexo7, anexo1)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntervencaoControllerApi->upload_lote_intervencoes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **anexo9** | **str**|  | 
 **anexo10** | **str**|  | 
 **anexo2** | **str**|  | 
 **arquivo_dados** | **str**|  | 
 **anexo8** | **str**|  | 
 **anexo4** | **str**|  | 
 **anexo5** | **str**|  | 
 **anexo3** | **str**|  | 
 **anexo6** | **str**|  | 
 **anexo7** | **str**|  | 
 **anexo1** | **str**|  | 

### Return type

[**RespostaUploadIntervencoesDto**](RespostaUploadIntervencoesDto.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

