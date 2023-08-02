# swagger_client.EmpresaApi

All URIs are relative to *https://integra.ons.org.br/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**empresa_listar_empresas_representadas**](EmpresaApi.md#empresa_listar_empresas_representadas) | **GET** /programacao/empresasrepresentadas | Listar dados das Empresas representadas pelo usuário

# **empresa_listar_empresas_representadas**
> EmpresaResponse empresa_listar_empresas_representadas()

Listar dados das Empresas representadas pelo usuário

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
api_instance = swagger_client.EmpresaApi(swagger_client.ApiClient(configuration))

try:
    # Listar dados das Empresas representadas pelo usuário
    api_response = api_instance.empresa_listar_empresas_representadas()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmpresaApi->empresa_listar_empresas_representadas: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**EmpresaResponse**](EmpresaResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

