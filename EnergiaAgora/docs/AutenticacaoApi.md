# swagger_client.AutenticacaoApi

All URIs are relative to *https://integra.ons.org.br/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_autenticar**](AutenticacaoApi.md#post_autenticar) | **POST** /autenticar | 
[**post_renovar**](AutenticacaoApi.md#post_renovar) | **POST** /renovar | 

# **post_autenticar**
> ResultadoAutenticacao post_autenticar(body)



Obter o token de autenticação para utilização da API.    O usuário e senha devem ser os mesmos utilizados para se autenticar no SINTEGRE, mas para obter acesso aos dados da API, a permissão deve ser solicitada em: <a href='https://sintegre.ons.org.br/paginas/meu-perfil/meus-sistemas.aspx' target='_blank'>Meus sistemas</a>         Processo: Previsão e acompanhamento da carga   Sistema: APIAvaliacaoOperacao - API que fornece dados de avaliação da operação        O acesso sera concedido após a aprovação do gestor do processo.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AutenticacaoApi()
body = swagger_client.Autenticar() # Autenticar | 

try:
    api_response = api_instance.post_autenticar(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutenticacaoApi->post_autenticar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Autenticar**](Autenticar.md)|  | 

### Return type

[**ResultadoAutenticacao**](ResultadoAutenticacao.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_renovar**
> ResultadoAutenticacao post_renovar(body)



Renovar o token de autenticação para utilização da API

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AutenticacaoApi()
body = swagger_client.Renovar() # Renovar | Refresh token gerado na autenticação

try:
    api_response = api_instance.post_renovar(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutenticacaoApi->post_renovar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Renovar**](Renovar.md)| Refresh token gerado na autenticação | 

### Return type

[**ResultadoAutenticacao**](ResultadoAutenticacao.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

