# swagger_client.GrandezasVerificadasApi

All URIs are relative to *https://integra.ons.org.br/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_afluencia_reservatorio**](GrandezasVerificadasApi.md#get_afluencia_reservatorio) | **GET** /hidrologia/reservatorios/{Identificador}/afluencia | 
[**get_defluencia_reservatorio**](GrandezasVerificadasApi.md#get_defluencia_reservatorio) | **GET** /hidrologia/reservatorios/{Identificador}/defluencia | 
[**get_energia_turbinavel_reservatorio**](GrandezasVerificadasApi.md#get_energia_turbinavel_reservatorio) | **GET** /hidrologia/reservatorios/{Identificador}/energiaTurbinavel | 
[**get_nivel_jusante_reservatorio**](GrandezasVerificadasApi.md#get_nivel_jusante_reservatorio) | **GET** /hidrologia/reservatorios/{Identificador}/nivelJusante | 
[**get_nivel_montante_reservatorio**](GrandezasVerificadasApi.md#get_nivel_montante_reservatorio) | **GET** /hidrologia/reservatorios/{Identificador}/nivelMontante | 
[**get_vazao_outras_estruturas_reservatorio**](GrandezasVerificadasApi.md#get_vazao_outras_estruturas_reservatorio) | **GET** /hidrologia/reservatorios/{Identificador}/vazaoOutrasEstruturas | 
[**get_vazao_turbinada_reservatorio**](GrandezasVerificadasApi.md#get_vazao_turbinada_reservatorio) | **GET** /hidrologia/reservatorios/{Identificador}/vazaoTurbinada | 
[**get_vazao_vertida_reservatorio**](GrandezasVerificadasApi.md#get_vazao_vertida_reservatorio) | **GET** /hidrologia/reservatorios/{Identificador}/vazaoVertida | 
[**get_volume_util_reservatorio**](GrandezasVerificadasApi.md#get_volume_util_reservatorio) | **GET** /hidrologia/reservatorios/{Identificador}/volumeUtil | 

# **get_afluencia_reservatorio**
> ResultadoConsultaGrandezaPaginada get_afluencia_reservatorio(pagina, quantidade, identificador, inicio, fim, intervalo, origem=origem)



Obter os valores de vazao afluente () do reservatorio no periodo (máx 7 dias) e intervalo definidos

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
api_instance = swagger_client.GrandezasVerificadasApi(swagger_client.ApiClient(configuration))
pagina = 1 # int | Pagina corrente (default to 1)
quantidade = 240 # int | Quantidade de resultados por pagina (limitado a 240 itens por página) (default to 240)
identificador = 'identificador_example' # str | Identificador do Reservatorio
inicio = 'inicio_example' # str | Data de inicio do periodo (AAAA-MM-DD HH:mm:ss)
fim = 'fim_example' # str | Data de fim do periodo (AAAA-MM-DD HH:mm:ss)
intervalo = 'intervalo_example' # str | Intervalo de consolidacao dos dados (HO ou DI)
origem = 'origem_example' # str | Origem dos dados (TRL, SSC, FTP ou ATR) <li>TRL – Tempo Real <li>SSC – Tempo Real Lido do Sistema de Supervisão <li>FTP – Tempo Real Lido do Servidor FTP <li>ATR – Valor atribuído. (optional)

try:
    api_response = api_instance.get_afluencia_reservatorio(pagina, quantidade, identificador, inicio, fim, intervalo, origem=origem)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GrandezasVerificadasApi->get_afluencia_reservatorio: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pagina** | **int**| Pagina corrente | [default to 1]
 **quantidade** | **int**| Quantidade de resultados por pagina (limitado a 240 itens por página) | [default to 240]
 **identificador** | **str**| Identificador do Reservatorio | 
 **inicio** | **str**| Data de inicio do periodo (AAAA-MM-DD HH:mm:ss) | 
 **fim** | **str**| Data de fim do periodo (AAAA-MM-DD HH:mm:ss) | 
 **intervalo** | **str**| Intervalo de consolidacao dos dados (HO ou DI) | 
 **origem** | **str**| Origem dos dados (TRL, SSC, FTP ou ATR) &lt;li&gt;TRL – Tempo Real &lt;li&gt;SSC – Tempo Real Lido do Sistema de Supervisão &lt;li&gt;FTP – Tempo Real Lido do Servidor FTP &lt;li&gt;ATR – Valor atribuído. | [optional] 

### Return type

[**ResultadoConsultaGrandezaPaginada**](ResultadoConsultaGrandezaPaginada.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_defluencia_reservatorio**
> ResultadoConsultaGrandezaPaginada get_defluencia_reservatorio(pagina, quantidade, identificador, inicio, fim, intervalo, origem=origem)



Obter os valores de defluencia (m3/s) do reservatorio no periodo (máx 7 dias) e intervalo definidos

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
api_instance = swagger_client.GrandezasVerificadasApi(swagger_client.ApiClient(configuration))
pagina = 1 # int | Pagina corrente (default to 1)
quantidade = 240 # int | Quantidade de resultados por pagina (limitado a 240 itens por página) (default to 240)
identificador = 'identificador_example' # str | Identificador do Reservatorio
inicio = 'inicio_example' # str | Data de inicio do periodo (AAAA-MM-DD HH:mm:ss)
fim = 'fim_example' # str | Data de fim do periodo (AAAA-MM-DD HH:mm:ss)
intervalo = 'intervalo_example' # str | Intervalo de consolidacao dos dados (HO ou DI)
origem = 'origem_example' # str | Origem dos dados (TRL, SSC, FTP ou ATR) <li>TRL – Tempo Real <li>SSC – Tempo Real Lido do Sistema de Supervisão <li>FTP – Tempo Real Lido do Servidor FTP <li>ATR – Valor atribuído. (optional)

try:
    api_response = api_instance.get_defluencia_reservatorio(pagina, quantidade, identificador, inicio, fim, intervalo, origem=origem)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GrandezasVerificadasApi->get_defluencia_reservatorio: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pagina** | **int**| Pagina corrente | [default to 1]
 **quantidade** | **int**| Quantidade de resultados por pagina (limitado a 240 itens por página) | [default to 240]
 **identificador** | **str**| Identificador do Reservatorio | 
 **inicio** | **str**| Data de inicio do periodo (AAAA-MM-DD HH:mm:ss) | 
 **fim** | **str**| Data de fim do periodo (AAAA-MM-DD HH:mm:ss) | 
 **intervalo** | **str**| Intervalo de consolidacao dos dados (HO ou DI) | 
 **origem** | **str**| Origem dos dados (TRL, SSC, FTP ou ATR) &lt;li&gt;TRL – Tempo Real &lt;li&gt;SSC – Tempo Real Lido do Sistema de Supervisão &lt;li&gt;FTP – Tempo Real Lido do Servidor FTP &lt;li&gt;ATR – Valor atribuído. | [optional] 

### Return type

[**ResultadoConsultaGrandezaPaginada**](ResultadoConsultaGrandezaPaginada.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_energia_turbinavel_reservatorio**
> ResultadoConsultaGrandezaPaginada get_energia_turbinavel_reservatorio(pagina, quantidade, identificador, inicio, fim, intervalo, origem=origem)



Obter os valores de vazao transferida () do reservatorio no periodo (máx 7 dias) e intervalo definidos

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
api_instance = swagger_client.GrandezasVerificadasApi(swagger_client.ApiClient(configuration))
pagina = 1 # int | Pagina corrente (default to 1)
quantidade = 240 # int | Quantidade de resultados por pagina (limitado a 240 itens por página) (default to 240)
identificador = 'identificador_example' # str | Identificador do Reservatorio
inicio = 'inicio_example' # str | Data de inicio do periodo (AAAA-MM-DD HH:mm:ss)
fim = 'fim_example' # str | Data de fim do periodo (AAAA-MM-DD HH:mm:ss)
intervalo = 'intervalo_example' # str | Intervalo de consolidacao dos dados (HO ou DI)
origem = 'origem_example' # str | Origem dos dados (TRL, SSC, FTP ou ATR) <li>TRL – Tempo Real <li>SSC – Tempo Real Lido do Sistema de Supervisão <li>FTP – Tempo Real Lido do Servidor FTP <li>ATR – Valor atribuído. (optional)

try:
    api_response = api_instance.get_energia_turbinavel_reservatorio(pagina, quantidade, identificador, inicio, fim, intervalo, origem=origem)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GrandezasVerificadasApi->get_energia_turbinavel_reservatorio: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pagina** | **int**| Pagina corrente | [default to 1]
 **quantidade** | **int**| Quantidade de resultados por pagina (limitado a 240 itens por página) | [default to 240]
 **identificador** | **str**| Identificador do Reservatorio | 
 **inicio** | **str**| Data de inicio do periodo (AAAA-MM-DD HH:mm:ss) | 
 **fim** | **str**| Data de fim do periodo (AAAA-MM-DD HH:mm:ss) | 
 **intervalo** | **str**| Intervalo de consolidacao dos dados (HO ou DI) | 
 **origem** | **str**| Origem dos dados (TRL, SSC, FTP ou ATR) &lt;li&gt;TRL – Tempo Real &lt;li&gt;SSC – Tempo Real Lido do Sistema de Supervisão &lt;li&gt;FTP – Tempo Real Lido do Servidor FTP &lt;li&gt;ATR – Valor atribuído. | [optional] 

### Return type

[**ResultadoConsultaGrandezaPaginada**](ResultadoConsultaGrandezaPaginada.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nivel_jusante_reservatorio**
> ResultadoConsultaGrandezaPaginada get_nivel_jusante_reservatorio(pagina, quantidade, identificador, inicio, fim, intervalo, origem=origem)



Obter os valores de nivel de jusante () do reservatorio no periodo (máx 7 dias) e intervalo definidos

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
api_instance = swagger_client.GrandezasVerificadasApi(swagger_client.ApiClient(configuration))
pagina = 1 # int | Pagina corrente (default to 1)
quantidade = 240 # int | Quantidade de resultados por pagina (limitado a 240 itens por página) (default to 240)
identificador = 'identificador_example' # str | Identificador do Reservatorio
inicio = 'inicio_example' # str | Data de inicio do periodo (AAAA-MM-DD HH:mm:ss)
fim = 'fim_example' # str | Data de fim do periodo (AAAA-MM-DD HH:mm:ss)
intervalo = 'intervalo_example' # str | Intervalo de consolidacao dos dados (HO ou DI)
origem = 'origem_example' # str | Origem dos dados (TRL, SSC, FTP ou ATR) <li>TRL – Tempo Real <li>SSC – Tempo Real Lido do Sistema de Supervisão <li>FTP – Tempo Real Lido do Servidor FTP <li>ATR – Valor atribuído. (optional)

try:
    api_response = api_instance.get_nivel_jusante_reservatorio(pagina, quantidade, identificador, inicio, fim, intervalo, origem=origem)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GrandezasVerificadasApi->get_nivel_jusante_reservatorio: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pagina** | **int**| Pagina corrente | [default to 1]
 **quantidade** | **int**| Quantidade de resultados por pagina (limitado a 240 itens por página) | [default to 240]
 **identificador** | **str**| Identificador do Reservatorio | 
 **inicio** | **str**| Data de inicio do periodo (AAAA-MM-DD HH:mm:ss) | 
 **fim** | **str**| Data de fim do periodo (AAAA-MM-DD HH:mm:ss) | 
 **intervalo** | **str**| Intervalo de consolidacao dos dados (HO ou DI) | 
 **origem** | **str**| Origem dos dados (TRL, SSC, FTP ou ATR) &lt;li&gt;TRL – Tempo Real &lt;li&gt;SSC – Tempo Real Lido do Sistema de Supervisão &lt;li&gt;FTP – Tempo Real Lido do Servidor FTP &lt;li&gt;ATR – Valor atribuído. | [optional] 

### Return type

[**ResultadoConsultaGrandezaPaginada**](ResultadoConsultaGrandezaPaginada.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nivel_montante_reservatorio**
> ResultadoConsultaGrandezaPaginada get_nivel_montante_reservatorio(pagina, quantidade, identificador, inicio, fim, intervalo, origem=origem)



Obter os valores de nivel de montante () do reservatorio no periodo (máx 7 dias) e intervalo definidos

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
api_instance = swagger_client.GrandezasVerificadasApi(swagger_client.ApiClient(configuration))
pagina = 1 # int | Pagina corrente (default to 1)
quantidade = 240 # int | Quantidade de resultados por pagina (limitado a 240 itens por página) (default to 240)
identificador = 'identificador_example' # str | Identificador do Reservatorio
inicio = 'inicio_example' # str | Data de inicio do periodo (AAAA-MM-DD HH:mm:ss)
fim = 'fim_example' # str | Data de fim do periodo (AAAA-MM-DD HH:mm:ss)
intervalo = 'intervalo_example' # str | Intervalo de consolidacao dos dados (HO ou DI)
origem = 'origem_example' # str | Origem dos dados (TRL, SSC, FTP ou ATR) <li>TRL – Tempo Real <li>SSC – Tempo Real Lido do Sistema de Supervisão <li>FTP – Tempo Real Lido do Servidor FTP <li>ATR – Valor atribuído. (optional)

try:
    api_response = api_instance.get_nivel_montante_reservatorio(pagina, quantidade, identificador, inicio, fim, intervalo, origem=origem)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GrandezasVerificadasApi->get_nivel_montante_reservatorio: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pagina** | **int**| Pagina corrente | [default to 1]
 **quantidade** | **int**| Quantidade de resultados por pagina (limitado a 240 itens por página) | [default to 240]
 **identificador** | **str**| Identificador do Reservatorio | 
 **inicio** | **str**| Data de inicio do periodo (AAAA-MM-DD HH:mm:ss) | 
 **fim** | **str**| Data de fim do periodo (AAAA-MM-DD HH:mm:ss) | 
 **intervalo** | **str**| Intervalo de consolidacao dos dados (HO ou DI) | 
 **origem** | **str**| Origem dos dados (TRL, SSC, FTP ou ATR) &lt;li&gt;TRL – Tempo Real &lt;li&gt;SSC – Tempo Real Lido do Sistema de Supervisão &lt;li&gt;FTP – Tempo Real Lido do Servidor FTP &lt;li&gt;ATR – Valor atribuído. | [optional] 

### Return type

[**ResultadoConsultaGrandezaPaginada**](ResultadoConsultaGrandezaPaginada.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vazao_outras_estruturas_reservatorio**
> ResultadoConsultaGrandezaPaginada get_vazao_outras_estruturas_reservatorio(pagina, quantidade, identificador, inicio, fim, intervalo, origem=origem)



Obter os valores de vazao de outras estruturas () do reservatorio (máx 7 dias) no periodo e intervalo definidos

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
api_instance = swagger_client.GrandezasVerificadasApi(swagger_client.ApiClient(configuration))
pagina = 1 # int | Pagina corrente (default to 1)
quantidade = 240 # int | Quantidade de resultados por pagina (limitado a 240 itens por página) (default to 240)
identificador = 'identificador_example' # str | Identificador do Reservatorio
inicio = 'inicio_example' # str | Data de inicio do periodo (AAAA-MM-DD HH:mm:ss)
fim = 'fim_example' # str | Data de fim do periodo (AAAA-MM-DD HH:mm:ss)
intervalo = 'intervalo_example' # str | Intervalo de consolidacao dos dados (HO ou DI)
origem = 'origem_example' # str | Origem dos dados (TRL, SSC, FTP ou ATR) <li>TRL – Tempo Real <li>SSC – Tempo Real Lido do Sistema de Supervisão <li>FTP – Tempo Real Lido do Servidor FTP <li>ATR – Valor atribuído. (optional)

try:
    api_response = api_instance.get_vazao_outras_estruturas_reservatorio(pagina, quantidade, identificador, inicio, fim, intervalo, origem=origem)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GrandezasVerificadasApi->get_vazao_outras_estruturas_reservatorio: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pagina** | **int**| Pagina corrente | [default to 1]
 **quantidade** | **int**| Quantidade de resultados por pagina (limitado a 240 itens por página) | [default to 240]
 **identificador** | **str**| Identificador do Reservatorio | 
 **inicio** | **str**| Data de inicio do periodo (AAAA-MM-DD HH:mm:ss) | 
 **fim** | **str**| Data de fim do periodo (AAAA-MM-DD HH:mm:ss) | 
 **intervalo** | **str**| Intervalo de consolidacao dos dados (HO ou DI) | 
 **origem** | **str**| Origem dos dados (TRL, SSC, FTP ou ATR) &lt;li&gt;TRL – Tempo Real &lt;li&gt;SSC – Tempo Real Lido do Sistema de Supervisão &lt;li&gt;FTP – Tempo Real Lido do Servidor FTP &lt;li&gt;ATR – Valor atribuído. | [optional] 

### Return type

[**ResultadoConsultaGrandezaPaginada**](ResultadoConsultaGrandezaPaginada.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vazao_turbinada_reservatorio**
> ResultadoConsultaGrandezaPaginada get_vazao_turbinada_reservatorio(pagina, quantidade, identificador, inicio, fim, intervalo, origem=origem)



Obter os valores de vazao turbinada () do reservatorio no periodo (máx 7 dias) e intervalo definidos

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
api_instance = swagger_client.GrandezasVerificadasApi(swagger_client.ApiClient(configuration))
pagina = 1 # int | Pagina corrente (default to 1)
quantidade = 240 # int | Quantidade de resultados por pagina (limitado a 240 itens por página) (default to 240)
identificador = 'identificador_example' # str | Identificador do Reservatorio
inicio = 'inicio_example' # str | Data de inicio do periodo (AAAA-MM-DD HH:mm:ss)
fim = 'fim_example' # str | Data de fim do periodo (AAAA-MM-DD HH:mm:ss)
intervalo = 'intervalo_example' # str | Intervalo de consolidacao dos dados (HO ou DI)
origem = 'origem_example' # str | Origem dos dados (TRL, SSC, FTP ou ATR) <li>TRL – Tempo Real <li>SSC – Tempo Real Lido do Sistema de Supervisão <li>FTP – Tempo Real Lido do Servidor FTP <li>ATR – Valor atribuído. (optional)

try:
    api_response = api_instance.get_vazao_turbinada_reservatorio(pagina, quantidade, identificador, inicio, fim, intervalo, origem=origem)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GrandezasVerificadasApi->get_vazao_turbinada_reservatorio: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pagina** | **int**| Pagina corrente | [default to 1]
 **quantidade** | **int**| Quantidade de resultados por pagina (limitado a 240 itens por página) | [default to 240]
 **identificador** | **str**| Identificador do Reservatorio | 
 **inicio** | **str**| Data de inicio do periodo (AAAA-MM-DD HH:mm:ss) | 
 **fim** | **str**| Data de fim do periodo (AAAA-MM-DD HH:mm:ss) | 
 **intervalo** | **str**| Intervalo de consolidacao dos dados (HO ou DI) | 
 **origem** | **str**| Origem dos dados (TRL, SSC, FTP ou ATR) &lt;li&gt;TRL – Tempo Real &lt;li&gt;SSC – Tempo Real Lido do Sistema de Supervisão &lt;li&gt;FTP – Tempo Real Lido do Servidor FTP &lt;li&gt;ATR – Valor atribuído. | [optional] 

### Return type

[**ResultadoConsultaGrandezaPaginada**](ResultadoConsultaGrandezaPaginada.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vazao_vertida_reservatorio**
> ResultadoConsultaGrandezaPaginada get_vazao_vertida_reservatorio(pagina, quantidade, identificador, inicio, fim, intervalo, origem=origem)



Obter os valores de vazao vertida () do reservatorio no periodo (máx 7 dias) e intervalo definidos

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
api_instance = swagger_client.GrandezasVerificadasApi(swagger_client.ApiClient(configuration))
pagina = 1 # int | Pagina corrente (default to 1)
quantidade = 240 # int | Quantidade de resultados por pagina (limitado a 240 itens por página) (default to 240)
identificador = 'identificador_example' # str | Identificador do Reservatorio
inicio = 'inicio_example' # str | Data de inicio do periodo (AAAA-MM-DD HH:mm:ss)
fim = 'fim_example' # str | Data de fim do periodo (AAAA-MM-DD HH:mm:ss)
intervalo = 'intervalo_example' # str | Intervalo de consolidacao dos dados (HO ou DI)
origem = 'origem_example' # str | Origem dos dados (TRL, SSC, FTP ou ATR) <li>TRL – Tempo Real <li>SSC – Tempo Real Lido do Sistema de Supervisão <li>FTP – Tempo Real Lido do Servidor FTP <li>ATR – Valor atribuído. (optional)

try:
    api_response = api_instance.get_vazao_vertida_reservatorio(pagina, quantidade, identificador, inicio, fim, intervalo, origem=origem)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GrandezasVerificadasApi->get_vazao_vertida_reservatorio: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pagina** | **int**| Pagina corrente | [default to 1]
 **quantidade** | **int**| Quantidade de resultados por pagina (limitado a 240 itens por página) | [default to 240]
 **identificador** | **str**| Identificador do Reservatorio | 
 **inicio** | **str**| Data de inicio do periodo (AAAA-MM-DD HH:mm:ss) | 
 **fim** | **str**| Data de fim do periodo (AAAA-MM-DD HH:mm:ss) | 
 **intervalo** | **str**| Intervalo de consolidacao dos dados (HO ou DI) | 
 **origem** | **str**| Origem dos dados (TRL, SSC, FTP ou ATR) &lt;li&gt;TRL – Tempo Real &lt;li&gt;SSC – Tempo Real Lido do Sistema de Supervisão &lt;li&gt;FTP – Tempo Real Lido do Servidor FTP &lt;li&gt;ATR – Valor atribuído. | [optional] 

### Return type

[**ResultadoConsultaGrandezaPaginada**](ResultadoConsultaGrandezaPaginada.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_volume_util_reservatorio**
> ResultadoConsultaGrandezaPaginada get_volume_util_reservatorio(pagina, quantidade, identificador, inicio, fim, intervalo, origem=origem)



Obter os valores de volume util () do reservatorio no periodo e intervalo definidos (máx 7 dias)

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
api_instance = swagger_client.GrandezasVerificadasApi(swagger_client.ApiClient(configuration))
pagina = 1 # int | Pagina corrente (default to 1)
quantidade = 240 # int | Quantidade de resultados por pagina (limitado a 240 itens por página) (default to 240)
identificador = 'identificador_example' # str | Identificador do Reservatorio
inicio = 'inicio_example' # str | Data de inicio do periodo (AAAA-MM-DD HH:mm:ss)
fim = 'fim_example' # str | Data de fim do periodo (AAAA-MM-DD HH:mm:ss)
intervalo = 'intervalo_example' # str | Intervalo de consolidacao dos dados (HO ou DI)
origem = 'origem_example' # str | Origem dos dados (TRL, SSC, FTP ou ATR) <li>TRL – Tempo Real <li>SSC – Tempo Real Lido do Sistema de Supervisão <li>FTP – Tempo Real Lido do Servidor FTP <li>ATR – Valor atribuído. (optional)

try:
    api_response = api_instance.get_volume_util_reservatorio(pagina, quantidade, identificador, inicio, fim, intervalo, origem=origem)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GrandezasVerificadasApi->get_volume_util_reservatorio: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pagina** | **int**| Pagina corrente | [default to 1]
 **quantidade** | **int**| Quantidade de resultados por pagina (limitado a 240 itens por página) | [default to 240]
 **identificador** | **str**| Identificador do Reservatorio | 
 **inicio** | **str**| Data de inicio do periodo (AAAA-MM-DD HH:mm:ss) | 
 **fim** | **str**| Data de fim do periodo (AAAA-MM-DD HH:mm:ss) | 
 **intervalo** | **str**| Intervalo de consolidacao dos dados (HO ou DI) | 
 **origem** | **str**| Origem dos dados (TRL, SSC, FTP ou ATR) &lt;li&gt;TRL – Tempo Real &lt;li&gt;SSC – Tempo Real Lido do Sistema de Supervisão &lt;li&gt;FTP – Tempo Real Lido do Servidor FTP &lt;li&gt;ATR – Valor atribuído. | [optional] 

### Return type

[**ResultadoConsultaGrandezaPaginada**](ResultadoConsultaGrandezaPaginada.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

