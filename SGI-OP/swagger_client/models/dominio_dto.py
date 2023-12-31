# coding: utf-8

"""
    Integração com o SGI-OP

    Api de integração com os dados dos SGI-OP.  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class DominioDto(object):
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
        'valor': 'str',
        'texto': 'str'
    }

    attribute_map = {
        'valor': 'valor',
        'texto': 'texto'
    }

    def __init__(self, valor=None, texto=None):  # noqa: E501
        """DominioDto - a model defined in Swagger"""  # noqa: E501
        self._valor = None
        self._texto = None
        self.discriminator = None
        self.valor = valor
        self.texto = texto

    @property
    def valor(self):
        """Gets the valor of this DominioDto.  # noqa: E501

        Valor do domínio.  # noqa: E501

        :return: The valor of this DominioDto.  # noqa: E501
        :rtype: str
        """
        return self._valor

    @valor.setter
    def valor(self, valor):
        """Sets the valor of this DominioDto.

        Valor do domínio.  # noqa: E501

        :param valor: The valor of this DominioDto.  # noqa: E501
        :type: str
        """
        if valor is None:
            raise ValueError("Invalid value for `valor`, must not be `None`")  # noqa: E501

        self._valor = valor

    @property
    def texto(self):
        """Gets the texto of this DominioDto.  # noqa: E501

        Texto do domínio.  # noqa: E501

        :return: The texto of this DominioDto.  # noqa: E501
        :rtype: str
        """
        return self._texto

    @texto.setter
    def texto(self, texto):
        """Sets the texto of this DominioDto.

        Texto do domínio.  # noqa: E501

        :param texto: The texto of this DominioDto.  # noqa: E501
        :type: str
        """
        if texto is None:
            raise ValueError("Invalid value for `texto`, must not be `None`")  # noqa: E501

        self._texto = texto

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
        if issubclass(DominioDto, dict):
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
        if not isinstance(other, DominioDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
