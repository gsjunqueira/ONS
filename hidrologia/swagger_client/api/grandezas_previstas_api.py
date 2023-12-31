# coding: utf-8

"""
    Hidrologia

    API que fornece dados hidrológicos  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class GrandezasPrevistasApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def consultar_previsoes(self, reservatorio, data_inicio_previsao, data_validade_previsao, **kwargs):  # noqa: E501
        """Realiza a consulta das previsões das vazões diárias por reservatório.  # noqa: E501

        Realiza a consulta das previsões das vazões diárias por reservatório.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.consultar_previsoes(reservatorio, data_inicio_previsao, data_validade_previsao, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str reservatorio: identificador do reservatório. (required)
        :param datetime data_inicio_previsao: data de início da previsão  (AAAA-MM-DD). (required)
        :param list[date] data_validade_previsao: datas de validade da previsão (AAAA-MM-DD). (required)
        :param int pagina: página para recuperação das previsões.
        :param int quantidade: quantidade por página.
        :return: ResultadoPrevisaoReservatorio
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.consultar_previsoes_with_http_info(reservatorio, data_inicio_previsao, data_validade_previsao, **kwargs)  # noqa: E501
        else:
            (data) = self.consultar_previsoes_with_http_info(reservatorio, data_inicio_previsao, data_validade_previsao, **kwargs)  # noqa: E501
            return data

    def consultar_previsoes_with_http_info(self, reservatorio, data_inicio_previsao, data_validade_previsao, **kwargs):  # noqa: E501
        """Realiza a consulta das previsões das vazões diárias por reservatório.  # noqa: E501

        Realiza a consulta das previsões das vazões diárias por reservatório.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.consultar_previsoes_with_http_info(reservatorio, data_inicio_previsao, data_validade_previsao, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str reservatorio: identificador do reservatório. (required)
        :param datetime data_inicio_previsao: data de início da previsão  (AAAA-MM-DD). (required)
        :param list[date] data_validade_previsao: datas de validade da previsão (AAAA-MM-DD). (required)
        :param int pagina: página para recuperação das previsões.
        :param int quantidade: quantidade por página.
        :return: ResultadoPrevisaoReservatorio
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['reservatorio', 'data_inicio_previsao', 'data_validade_previsao', 'pagina', 'quantidade']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method consultar_previsoes" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'reservatorio' is set
        if ('reservatorio' not in params or
                params['reservatorio'] is None):
            raise ValueError("Missing the required parameter `reservatorio` when calling `consultar_previsoes`")  # noqa: E501
        # verify the required parameter 'data_inicio_previsao' is set
        if ('data_inicio_previsao' not in params or
                params['data_inicio_previsao'] is None):
            raise ValueError("Missing the required parameter `data_inicio_previsao` when calling `consultar_previsoes`")  # noqa: E501
        # verify the required parameter 'data_validade_previsao' is set
        if ('data_validade_previsao' not in params or
                params['data_validade_previsao'] is None):
            raise ValueError("Missing the required parameter `data_validade_previsao` when calling `consultar_previsoes`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'reservatorio' in params:
            path_params['reservatorio'] = params['reservatorio']  # noqa: E501

        query_params = []
        if 'data_inicio_previsao' in params:
            query_params.append(('dataInicioPrevisao', params['data_inicio_previsao']))  # noqa: E501
        if 'data_validade_previsao' in params:
            query_params.append(('dataValidadePrevisao', params['data_validade_previsao']))  # noqa: E501
            collection_formats['dataValidadePrevisao'] = 'multi'  # noqa: E501
        if 'pagina' in params:
            query_params.append(('pagina', params['pagina']))  # noqa: E501
        if 'quantidade' in params:
            query_params.append(('quantidade', params['quantidade']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml', 'text/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/hidrologia/previsoes/{reservatorio}/vazao-diaria', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResultadoPrevisaoReservatorio',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
