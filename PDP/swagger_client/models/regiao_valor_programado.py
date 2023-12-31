# coding: utf-8

"""
    API para Programação Diária de Produção (PDP).

    API do PDP para obtenção de dados e informações sobre programação diária de produção.  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class RegiaoValorProgramado(object):
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
        'regiao': 'str',
        'valor': 'int'
    }

    attribute_map = {
        'regiao': 'Regiao',
        'valor': 'Valor'
    }

    def __init__(self, regiao=None, valor=None):  # noqa: E501
        """RegiaoValorProgramado - a model defined in Swagger"""  # noqa: E501
        self._regiao = None
        self._valor = None
        self.discriminator = None
        self.regiao = regiao
        self.valor = valor

    @property
    def regiao(self):
        """Gets the regiao of this RegiaoValorProgramado.  # noqa: E501


        :return: The regiao of this RegiaoValorProgramado.  # noqa: E501
        :rtype: str
        """
        return self._regiao

    @regiao.setter
    def regiao(self, regiao):
        """Sets the regiao of this RegiaoValorProgramado.


        :param regiao: The regiao of this RegiaoValorProgramado.  # noqa: E501
        :type: str
        """
        if regiao is None:
            raise ValueError("Invalid value for `regiao`, must not be `None`")  # noqa: E501

        self._regiao = regiao

    @property
    def valor(self):
        """Gets the valor of this RegiaoValorProgramado.  # noqa: E501


        :return: The valor of this RegiaoValorProgramado.  # noqa: E501
        :rtype: int
        """
        return self._valor

    @valor.setter
    def valor(self, valor):
        """Sets the valor of this RegiaoValorProgramado.


        :param valor: The valor of this RegiaoValorProgramado.  # noqa: E501
        :type: int
        """
        if valor is None:
            raise ValueError("Invalid value for `valor`, must not be `None`")  # noqa: E501

        self._valor = valor

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
        if issubclass(RegiaoValorProgramado, dict):
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
        if not isinstance(other, RegiaoValorProgramado):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
