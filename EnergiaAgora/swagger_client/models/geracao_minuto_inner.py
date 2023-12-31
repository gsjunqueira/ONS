# coding: utf-8

"""
    API Energia Agora

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: sta-integracao-tec@ons.org.br
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class GeracaoMinutoInner(object):
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
        'instante': 'datetime',
        'geracao': 'float'
    }

    attribute_map = {
        'instante': 'instante',
        'geracao': 'geracao'
    }

    def __init__(self, instante=None, geracao=None):  # noqa: E501
        """GeracaoMinutoInner - a model defined in Swagger"""  # noqa: E501
        self._instante = None
        self._geracao = None
        self.discriminator = None
        if instante is not None:
            self.instante = instante
        if geracao is not None:
            self.geracao = geracao

    @property
    def instante(self):
        """Gets the instante of this GeracaoMinutoInner.  # noqa: E501

        Instante da medição  # noqa: E501

        :return: The instante of this GeracaoMinutoInner.  # noqa: E501
        :rtype: datetime
        """
        return self._instante

    @instante.setter
    def instante(self, instante):
        """Sets the instante of this GeracaoMinutoInner.

        Instante da medição  # noqa: E501

        :param instante: The instante of this GeracaoMinutoInner.  # noqa: E501
        :type: datetime
        """

        self._instante = instante

    @property
    def geracao(self):
        """Gets the geracao of this GeracaoMinutoInner.  # noqa: E501

        Geração em MW  # noqa: E501

        :return: The geracao of this GeracaoMinutoInner.  # noqa: E501
        :rtype: float
        """
        return self._geracao

    @geracao.setter
    def geracao(self, geracao):
        """Sets the geracao of this GeracaoMinutoInner.

        Geração em MW  # noqa: E501

        :param geracao: The geracao of this GeracaoMinutoInner.  # noqa: E501
        :type: float
        """

        self._geracao = geracao

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
        if issubclass(GeracaoMinutoInner, dict):
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
        if not isinstance(other, GeracaoMinutoInner):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
