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

class Precipitacao(object):
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
        'identificador_estacao_meteo': 'str',
        'data_hora_medicao': 'str',
        'valor_medicao': 'str',
        'status_medicao': 'str',
        'furo_temporal': 'str',
        'estimado': 'str'
    }

    attribute_map = {
        'identificador_estacao_meteo': 'IdentificadorEstacaoMeteo',
        'data_hora_medicao': 'DataHoraMedicao',
        'valor_medicao': 'ValorMedicao',
        'status_medicao': 'StatusMedicao',
        'furo_temporal': 'FuroTemporal',
        'estimado': 'Estimado'
    }

    def __init__(self, identificador_estacao_meteo=None, data_hora_medicao=None, valor_medicao=None, status_medicao=None, furo_temporal=None, estimado=None):  # noqa: E501
        """Precipitacao - a model defined in Swagger"""  # noqa: E501
        self._identificador_estacao_meteo = None
        self._data_hora_medicao = None
        self._valor_medicao = None
        self._status_medicao = None
        self._furo_temporal = None
        self._estimado = None
        self.discriminator = None
        if identificador_estacao_meteo is not None:
            self.identificador_estacao_meteo = identificador_estacao_meteo
        if data_hora_medicao is not None:
            self.data_hora_medicao = data_hora_medicao
        if valor_medicao is not None:
            self.valor_medicao = valor_medicao
        if status_medicao is not None:
            self.status_medicao = status_medicao
        if furo_temporal is not None:
            self.furo_temporal = furo_temporal
        if estimado is not None:
            self.estimado = estimado

    @property
    def identificador_estacao_meteo(self):
        """Gets the identificador_estacao_meteo of this Precipitacao.  # noqa: E501


        :return: The identificador_estacao_meteo of this Precipitacao.  # noqa: E501
        :rtype: str
        """
        return self._identificador_estacao_meteo

    @identificador_estacao_meteo.setter
    def identificador_estacao_meteo(self, identificador_estacao_meteo):
        """Sets the identificador_estacao_meteo of this Precipitacao.


        :param identificador_estacao_meteo: The identificador_estacao_meteo of this Precipitacao.  # noqa: E501
        :type: str
        """

        self._identificador_estacao_meteo = identificador_estacao_meteo

    @property
    def data_hora_medicao(self):
        """Gets the data_hora_medicao of this Precipitacao.  # noqa: E501


        :return: The data_hora_medicao of this Precipitacao.  # noqa: E501
        :rtype: str
        """
        return self._data_hora_medicao

    @data_hora_medicao.setter
    def data_hora_medicao(self, data_hora_medicao):
        """Sets the data_hora_medicao of this Precipitacao.


        :param data_hora_medicao: The data_hora_medicao of this Precipitacao.  # noqa: E501
        :type: str
        """

        self._data_hora_medicao = data_hora_medicao

    @property
    def valor_medicao(self):
        """Gets the valor_medicao of this Precipitacao.  # noqa: E501


        :return: The valor_medicao of this Precipitacao.  # noqa: E501
        :rtype: str
        """
        return self._valor_medicao

    @valor_medicao.setter
    def valor_medicao(self, valor_medicao):
        """Sets the valor_medicao of this Precipitacao.


        :param valor_medicao: The valor_medicao of this Precipitacao.  # noqa: E501
        :type: str
        """

        self._valor_medicao = valor_medicao

    @property
    def status_medicao(self):
        """Gets the status_medicao of this Precipitacao.  # noqa: E501


        :return: The status_medicao of this Precipitacao.  # noqa: E501
        :rtype: str
        """
        return self._status_medicao

    @status_medicao.setter
    def status_medicao(self, status_medicao):
        """Sets the status_medicao of this Precipitacao.


        :param status_medicao: The status_medicao of this Precipitacao.  # noqa: E501
        :type: str
        """

        self._status_medicao = status_medicao

    @property
    def furo_temporal(self):
        """Gets the furo_temporal of this Precipitacao.  # noqa: E501


        :return: The furo_temporal of this Precipitacao.  # noqa: E501
        :rtype: str
        """
        return self._furo_temporal

    @furo_temporal.setter
    def furo_temporal(self, furo_temporal):
        """Sets the furo_temporal of this Precipitacao.


        :param furo_temporal: The furo_temporal of this Precipitacao.  # noqa: E501
        :type: str
        """

        self._furo_temporal = furo_temporal

    @property
    def estimado(self):
        """Gets the estimado of this Precipitacao.  # noqa: E501


        :return: The estimado of this Precipitacao.  # noqa: E501
        :rtype: str
        """
        return self._estimado

    @estimado.setter
    def estimado(self, estimado):
        """Sets the estimado of this Precipitacao.


        :param estimado: The estimado of this Precipitacao.  # noqa: E501
        :type: str
        """

        self._estimado = estimado

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
        if issubclass(Precipitacao, dict):
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
        if not isinstance(other, Precipitacao):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other