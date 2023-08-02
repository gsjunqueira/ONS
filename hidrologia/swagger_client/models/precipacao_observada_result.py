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

class PrecipacaoObservadaResult(object):
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
        'pagina': 'int',
        'quantidade': 'int',
        'resultados': 'list[Precipitacao]'
    }

    attribute_map = {
        'pagina': 'Pagina',
        'quantidade': 'Quantidade',
        'resultados': 'Resultados'
    }

    def __init__(self, pagina=None, quantidade=None, resultados=None):  # noqa: E501
        """PrecipacaoObservadaResult - a model defined in Swagger"""  # noqa: E501
        self._pagina = None
        self._quantidade = None
        self._resultados = None
        self.discriminator = None
        if pagina is not None:
            self.pagina = pagina
        if quantidade is not None:
            self.quantidade = quantidade
        if resultados is not None:
            self.resultados = resultados

    @property
    def pagina(self):
        """Gets the pagina of this PrecipacaoObservadaResult.  # noqa: E501


        :return: The pagina of this PrecipacaoObservadaResult.  # noqa: E501
        :rtype: int
        """
        return self._pagina

    @pagina.setter
    def pagina(self, pagina):
        """Sets the pagina of this PrecipacaoObservadaResult.


        :param pagina: The pagina of this PrecipacaoObservadaResult.  # noqa: E501
        :type: int
        """

        self._pagina = pagina

    @property
    def quantidade(self):
        """Gets the quantidade of this PrecipacaoObservadaResult.  # noqa: E501


        :return: The quantidade of this PrecipacaoObservadaResult.  # noqa: E501
        :rtype: int
        """
        return self._quantidade

    @quantidade.setter
    def quantidade(self, quantidade):
        """Sets the quantidade of this PrecipacaoObservadaResult.


        :param quantidade: The quantidade of this PrecipacaoObservadaResult.  # noqa: E501
        :type: int
        """

        self._quantidade = quantidade

    @property
    def resultados(self):
        """Gets the resultados of this PrecipacaoObservadaResult.  # noqa: E501


        :return: The resultados of this PrecipacaoObservadaResult.  # noqa: E501
        :rtype: list[Precipitacao]
        """
        return self._resultados

    @resultados.setter
    def resultados(self, resultados):
        """Sets the resultados of this PrecipacaoObservadaResult.


        :param resultados: The resultados of this PrecipacaoObservadaResult.  # noqa: E501
        :type: list[Precipitacao]
        """

        self._resultados = resultados

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
        if issubclass(PrecipacaoObservadaResult, dict):
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
        if not isinstance(other, PrecipacaoObservadaResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
