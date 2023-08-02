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

class GrandezaHidrologica(object):
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
        'identificador': 'str',
        'data_hora_medicao': 'str',
        'valor_medicao': 'str',
        'status_medicao': 'str'
    }

    attribute_map = {
        'identificador': 'Identificador',
        'data_hora_medicao': 'DataHoraMedicao',
        'valor_medicao': 'ValorMedicao',
        'status_medicao': 'StatusMedicao'
    }

    def __init__(self, identificador=None, data_hora_medicao=None, valor_medicao=None, status_medicao=None):  # noqa: E501
        """GrandezaHidrologica - a model defined in Swagger"""  # noqa: E501
        self._identificador = None
        self._data_hora_medicao = None
        self._valor_medicao = None
        self._status_medicao = None
        self.discriminator = None
        if identificador is not None:
            self.identificador = identificador
        if data_hora_medicao is not None:
            self.data_hora_medicao = data_hora_medicao
        if valor_medicao is not None:
            self.valor_medicao = valor_medicao
        if status_medicao is not None:
            self.status_medicao = status_medicao

    @property
    def identificador(self):
        """Gets the identificador of this GrandezaHidrologica.  # noqa: E501


        :return: The identificador of this GrandezaHidrologica.  # noqa: E501
        :rtype: str
        """
        return self._identificador

    @identificador.setter
    def identificador(self, identificador):
        """Sets the identificador of this GrandezaHidrologica.


        :param identificador: The identificador of this GrandezaHidrologica.  # noqa: E501
        :type: str
        """

        self._identificador = identificador

    @property
    def data_hora_medicao(self):
        """Gets the data_hora_medicao of this GrandezaHidrologica.  # noqa: E501


        :return: The data_hora_medicao of this GrandezaHidrologica.  # noqa: E501
        :rtype: str
        """
        return self._data_hora_medicao

    @data_hora_medicao.setter
    def data_hora_medicao(self, data_hora_medicao):
        """Sets the data_hora_medicao of this GrandezaHidrologica.


        :param data_hora_medicao: The data_hora_medicao of this GrandezaHidrologica.  # noqa: E501
        :type: str
        """

        self._data_hora_medicao = data_hora_medicao

    @property
    def valor_medicao(self):
        """Gets the valor_medicao of this GrandezaHidrologica.  # noqa: E501


        :return: The valor_medicao of this GrandezaHidrologica.  # noqa: E501
        :rtype: str
        """
        return self._valor_medicao

    @valor_medicao.setter
    def valor_medicao(self, valor_medicao):
        """Sets the valor_medicao of this GrandezaHidrologica.


        :param valor_medicao: The valor_medicao of this GrandezaHidrologica.  # noqa: E501
        :type: str
        """

        self._valor_medicao = valor_medicao

    @property
    def status_medicao(self):
        """Gets the status_medicao of this GrandezaHidrologica.  # noqa: E501


        :return: The status_medicao of this GrandezaHidrologica.  # noqa: E501
        :rtype: str
        """
        return self._status_medicao

    @status_medicao.setter
    def status_medicao(self, status_medicao):
        """Sets the status_medicao of this GrandezaHidrologica.


        :param status_medicao: The status_medicao of this GrandezaHidrologica.  # noqa: E501
        :type: str
        """

        self._status_medicao = status_medicao

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
        if issubclass(GrandezaHidrologica, dict):
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
        if not isinstance(other, GrandezaHidrologica):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
