# coding: utf-8

"""
    API para Programação Diária de Produção (PDP).

    API do PDP para obtenção de dados e informações sobre programação diária de produção.  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class AutenticacaoApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def post_autenticar(self, body, **kwargs):  # noqa: E501
        """post_autenticar  # noqa: E501

        Obter o token de autenticação para utilização da API.    O usuário e senha devem ser os mesmos utilizados para se autenticar no SINTEGRE, mas para obter acesso aos dados da API, a permissão deve ser solicitada em: https://sintegre.ons.org.br/paginas/meu-perfil/meus-sistemas.aspx         Processo: Programação da operação   Sistema: PDP - Permite acesso aos agentes as API da Progrmação        O acesso sera concedido após a aprovação do gestor do processo.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_autenticar(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Autenticar body: (required)
        :return: ResultadoAutenticacao
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_autenticar_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.post_autenticar_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def post_autenticar_with_http_info(self, body, **kwargs):  # noqa: E501
        """post_autenticar  # noqa: E501

        Obter o token de autenticação para utilização da API.    O usuário e senha devem ser os mesmos utilizados para se autenticar no SINTEGRE, mas para obter acesso aos dados da API, a permissão deve ser solicitada em: https://sintegre.ons.org.br/paginas/meu-perfil/meus-sistemas.aspx         Processo: Programação da operação   Sistema: PDP - Permite acesso aos agentes as API da Progrmação        O acesso sera concedido após a aprovação do gestor do processo.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_autenticar_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Autenticar body: (required)
        :return: ResultadoAutenticacao
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_autenticar" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_autenticar`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/autenticar', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResultadoAutenticacao',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_renovar(self, body, **kwargs):  # noqa: E501
        """post_renovar  # noqa: E501

        Renovar o token de autenticação para utilização da API  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_renovar(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Renovar body: Refresh token gerado na autenticação (required)
        :return: ResultadoAutenticacao
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_renovar_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.post_renovar_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def post_renovar_with_http_info(self, body, **kwargs):  # noqa: E501
        """post_renovar  # noqa: E501

        Renovar o token de autenticação para utilização da API  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_renovar_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Renovar body: Refresh token gerado na autenticação (required)
        :return: ResultadoAutenticacao
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_renovar" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_renovar`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/renovar', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResultadoAutenticacao',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
