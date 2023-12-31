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

class HistoricoDto(object):
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
        'data': 'datetime',
        'ocorrencia': 'str',
        'usuario': 'str',
        'area': 'str',
        'situacao_anterior': 'str',
        'situacao_posterior': 'str',
        'periodo_observacoes': 'str'
    }

    attribute_map = {
        'data': 'data',
        'ocorrencia': 'ocorrencia',
        'usuario': 'usuario',
        'area': 'area',
        'situacao_anterior': 'situacao_Anterior',
        'situacao_posterior': 'situacao_Posterior',
        'periodo_observacoes': 'periodo_Observacoes'
    }

    def __init__(self, data=None, ocorrencia=None, usuario=None, area=None, situacao_anterior=None, situacao_posterior=None, periodo_observacoes=None):  # noqa: E501
        """HistoricoDto - a model defined in Swagger"""  # noqa: E501
        self._data = None
        self._ocorrencia = None
        self._usuario = None
        self._area = None
        self._situacao_anterior = None
        self._situacao_posterior = None
        self._periodo_observacoes = None
        self.discriminator = None
        if data is not None:
            self.data = data
        if ocorrencia is not None:
            self.ocorrencia = ocorrencia
        if usuario is not None:
            self.usuario = usuario
        if area is not None:
            self.area = area
        if situacao_anterior is not None:
            self.situacao_anterior = situacao_anterior
        if situacao_posterior is not None:
            self.situacao_posterior = situacao_posterior
        if periodo_observacoes is not None:
            self.periodo_observacoes = periodo_observacoes

    @property
    def data(self):
        """Gets the data of this HistoricoDto.  # noqa: E501

        Data da Ocorrência.  # noqa: E501

        :return: The data of this HistoricoDto.  # noqa: E501
        :rtype: datetime
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this HistoricoDto.

        Data da Ocorrência.  # noqa: E501

        :param data: The data of this HistoricoDto.  # noqa: E501
        :type: datetime
        """

        self._data = data

    @property
    def ocorrencia(self):
        """Gets the ocorrencia of this HistoricoDto.  # noqa: E501

        Tipo da Ocorrencia.  # noqa: E501

        :return: The ocorrencia of this HistoricoDto.  # noqa: E501
        :rtype: str
        """
        return self._ocorrencia

    @ocorrencia.setter
    def ocorrencia(self, ocorrencia):
        """Sets the ocorrencia of this HistoricoDto.

        Tipo da Ocorrencia.  # noqa: E501

        :param ocorrencia: The ocorrencia of this HistoricoDto.  # noqa: E501
        :type: str
        """

        self._ocorrencia = ocorrencia

    @property
    def usuario(self):
        """Gets the usuario of this HistoricoDto.  # noqa: E501

        Nome do Usuario  # noqa: E501

        :return: The usuario of this HistoricoDto.  # noqa: E501
        :rtype: str
        """
        return self._usuario

    @usuario.setter
    def usuario(self, usuario):
        """Sets the usuario of this HistoricoDto.

        Nome do Usuario  # noqa: E501

        :param usuario: The usuario of this HistoricoDto.  # noqa: E501
        :type: str
        """

        self._usuario = usuario

    @property
    def area(self):
        """Gets the area of this HistoricoDto.  # noqa: E501

        Area.  # noqa: E501

        :return: The area of this HistoricoDto.  # noqa: E501
        :rtype: str
        """
        return self._area

    @area.setter
    def area(self, area):
        """Sets the area of this HistoricoDto.

        Area.  # noqa: E501

        :param area: The area of this HistoricoDto.  # noqa: E501
        :type: str
        """

        self._area = area

    @property
    def situacao_anterior(self):
        """Gets the situacao_anterior of this HistoricoDto.  # noqa: E501

        Situacao_Anterior.  # noqa: E501

        :return: The situacao_anterior of this HistoricoDto.  # noqa: E501
        :rtype: str
        """
        return self._situacao_anterior

    @situacao_anterior.setter
    def situacao_anterior(self, situacao_anterior):
        """Sets the situacao_anterior of this HistoricoDto.

        Situacao_Anterior.  # noqa: E501

        :param situacao_anterior: The situacao_anterior of this HistoricoDto.  # noqa: E501
        :type: str
        """

        self._situacao_anterior = situacao_anterior

    @property
    def situacao_posterior(self):
        """Gets the situacao_posterior of this HistoricoDto.  # noqa: E501

        Situacao Posterior  # noqa: E501

        :return: The situacao_posterior of this HistoricoDto.  # noqa: E501
        :rtype: str
        """
        return self._situacao_posterior

    @situacao_posterior.setter
    def situacao_posterior(self, situacao_posterior):
        """Sets the situacao_posterior of this HistoricoDto.

        Situacao Posterior  # noqa: E501

        :param situacao_posterior: The situacao_posterior of this HistoricoDto.  # noqa: E501
        :type: str
        """

        self._situacao_posterior = situacao_posterior

    @property
    def periodo_observacoes(self):
        """Gets the periodo_observacoes of this HistoricoDto.  # noqa: E501

        Periodo_Observacoes  # noqa: E501

        :return: The periodo_observacoes of this HistoricoDto.  # noqa: E501
        :rtype: str
        """
        return self._periodo_observacoes

    @periodo_observacoes.setter
    def periodo_observacoes(self, periodo_observacoes):
        """Sets the periodo_observacoes of this HistoricoDto.

        Periodo_Observacoes  # noqa: E501

        :param periodo_observacoes: The periodo_observacoes of this HistoricoDto.  # noqa: E501
        :type: str
        """

        self._periodo_observacoes = periodo_observacoes

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
        if issubclass(HistoricoDto, dict):
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
        if not isinstance(other, HistoricoDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
