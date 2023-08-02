# coding: utf-8

"""
    Hidrologia

    API que fornece dados hidrológicos  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Paginacao(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'pagina_corrente': 'int',
        'quantidade_total_itens': 'int'
    }

    attribute_map = {
        'pagina_corrente': 'PaginaCorrente',
        'quantidade_total_itens': 'QuantidadeTotalItens'
    }

    def __init__(self, pagina_corrente=None, quantidade_total_itens=None):  # noqa: E501
        """Paginacao - a model defined in Swagger"""  # noqa: E501
        self._pagina_corrente = None
        self._quantidade_total_itens = None
        self.discriminator = None
        if pagina_corrente is not None:
            self.pagina_corrente = pagina_corrente
        if quantidade_total_itens is not None:
            self.quantidade_total_itens = quantidade_total_itens

    @property
    def pagina_corrente(self):
        """Gets the pagina_corrente of this Paginacao.  # noqa: E501

        Pagina atual da consulta  # noqa: E501

        :return: The pagina_corrente of this Paginacao.  # noqa: E501
        :rtype: int
        """
        return self._pagina_corrente

    @pagina_corrente.setter
    def pagina_corrente(self, pagina_corrente):
        """Sets the pagina_corrente of this Paginacao.

        Pagina atual da consulta  # noqa: E501

        :param pagina_corrente: The pagina_corrente of this Paginacao.  # noqa: E501
        :type: int
        """

        self._pagina_corrente = pagina_corrente

    @property
    def quantidade_total_itens(self):
        """Gets the quantidade_total_itens of this Paginacao.  # noqa: E501

        Quantidade total de itens da consulta  # noqa: E501

        :return: The quantidade_total_itens of this Paginacao.  # noqa: E501
        :rtype: int
        """
        return self._quantidade_total_itens

    @quantidade_total_itens.setter
    def quantidade_total_itens(self, quantidade_total_itens):
        """Sets the quantidade_total_itens of this Paginacao.

        Quantidade total de itens da consulta  # noqa: E501

        :param quantidade_total_itens: The quantidade_total_itens of this Paginacao.  # noqa: E501
        :type: int
        """

        self._quantidade_total_itens = quantidade_total_itens

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Paginacao, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Paginacao):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other