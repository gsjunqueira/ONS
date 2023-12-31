# swagger-client
Api de integração com os dados dos SGI-OP.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: v1
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AutenticacaoApi(swagger_client.ApiClient(configuration))
body = swagger_client.Autenticar() # Autenticar | 

try:
    api_response = api_instance.post_autenticar(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutenticacaoApi->post_autenticar: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.AutenticacaoApi(swagger_client.ApiClient(configuration))
body = swagger_client.Renovar() # Renovar | Refresh token gerado na autenticação

try:
    api_response = api_instance.post_renovar(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutenticacaoApi->post_renovar: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://integra.ons.org.br/api*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AutenticacaoApi* | [**post_autenticar**](docs/AutenticacaoApi.md#post_autenticar) | **POST** /autenticar | 
*AutenticacaoApi* | [**post_renovar**](docs/AutenticacaoApi.md#post_renovar) | **POST** /renovar | 
*IntervencaoControllerApi* | [**consultar_dados_dominios_intervencao**](docs/IntervencaoControllerApi.md#consultar_dados_dominios_intervencao) | **GET** /sgi/dominios/{tipo} | Realiza a obtenção dos domínios em função do tipo recebido.
*IntervencaoControllerApi* | [**consultar_historico_dados_execucao**](docs/IntervencaoControllerApi.md#consultar_historico_dados_execucao) | **GET** /sgi/intervencoes/historico-execucao/{identificadorONS} | Realiza a obtenção do historico e dados de execução da intervenção com base no Identificador ONS informado
*IntervencaoControllerApi* | [**consultar_intervencoes_sgi**](docs/IntervencaoControllerApi.md#consultar_intervencoes_sgi) | **GET** /sgi/intervencoes | Realiza a obtenção das intervenções com base no filtro recebido.
*IntervencaoControllerApi* | [**consultar_situacao_importacao_lote**](docs/IntervencaoControllerApi.md#consultar_situacao_importacao_lote) | **GET** /sgi/intervencoes/importar-lote/{id} | Realiza a obtenção da situação de um lote de importação de intervençoes.
*IntervencaoControllerApi* | [**upload_lote_intervencoes**](docs/IntervencaoControllerApi.md#upload_lote_intervencoes) | **POST** /sgi/intervencoes/importar-lote | Realiza o processo de upload dos arquivos para criação das intervenções em lote.

## Documentation For Models

 - [Autenticar](docs/Autenticar.md)
 - [DadosExecucaoDto](docs/DadosExecucaoDto.md)
 - [DominioDto](docs/DominioDto.md)
 - [EquipamentoIntervencaoDto](docs/EquipamentoIntervencaoDto.md)
 - [ErroAutenticacao](docs/ErroAutenticacao.md)
 - [Error](docs/Error.md)
 - [HistoricoDto](docs/HistoricoDto.md)
 - [IntervencaoDto](docs/IntervencaoDto.md)
 - [IntervencoesImportarloteBody](docs/IntervencoesImportarloteBody.md)
 - [MensagemErroDto](docs/MensagemErroDto.md)
 - [Renovar](docs/Renovar.md)
 - [RespostaConsultaDominiosDto](docs/RespostaConsultaDominiosDto.md)
 - [RespostaConsultaIntervencaoDto](docs/RespostaConsultaIntervencaoDto.md)
 - [RespostaConsultaSituacaoImportacaoLoteDto](docs/RespostaConsultaSituacaoImportacaoLoteDto.md)
 - [RespostaErroPadraoDto](docs/RespostaErroPadraoDto.md)
 - [RespostaUploadIntervencoesDto](docs/RespostaUploadIntervencoesDto.md)
 - [ResultadoAutenticacao](docs/ResultadoAutenticacao.md)
 - [ResultadoHistoricoDadosExecucaoIntervencaoDto](docs/ResultadoHistoricoDadosExecucaoIntervencaoDto.md)

## Documentation For Authorization


## Bearer

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author


