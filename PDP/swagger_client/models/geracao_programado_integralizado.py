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

class GeracaoProgramadoIntegralizado(object):
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
        'geracoes_programadas': 'list[TipoUsinaValorProgramado]',
        'regiao': 'str',
        'regiao_descricao': 'str',
        'regiao_sigla': 'str',
        'ano': 'int',
        'mes': 'int',
        'dia': 'int'
    }

    attribute_map = {
        'geracoes_programadas': 'GeracoesProgramadas',
        'regiao': 'Regiao',
        'regiao_descricao': 'RegiaoDescricao',
        'regiao_sigla': 'RegiaoSigla',
        'ano': 'Ano',
        'mes': 'Mes',
        'dia': 'Dia'
    }

    def __init__(self, geracoes_programadas=None, regiao=None, regiao_descricao=None, regiao_sigla=None, ano=None, mes=None, dia=None):  # noqa: E501
        """GeracaoProgramadoIntegralizado - a model defined in Swagger"""  # noqa: E501
        self._geracoes_programadas = None
        self._regiao = None
        self._regiao_descricao = None
        self._regiao_sigla = None
        self._ano = None
        self._mes = None
        self._dia = None
        self.discriminator = None
        if geracoes_programadas is not None:
            self.geracoes_programadas = geracoes_programadas
        self.regiao = regiao
        if regiao_descricao is not None:
            self.regiao_descricao = regiao_descricao
        if regiao_sigla is not None:
            self.regiao_sigla = regiao_sigla
        self.ano = ano
        self.mes = mes
        self.dia = dia

    @property
    def geracoes_programadas(self):
        """Gets the geracoes_programadas of this GeracaoProgramadoIntegralizado.  # noqa: E501


        :return: The geracoes_programadas of this GeracaoProgramadoIntegralizado.  # noqa: E501
        :rtype: list[TipoUsinaValorProgramado]
        """
        return self._geracoes_programadas

    @geracoes_programadas.setter
    def geracoes_programadas(self, geracoes_programadas):
        """Sets the geracoes_programadas of this GeracaoProgramadoIntegralizado.


        :param geracoes_programadas: The geracoes_programadas of this GeracaoProgramadoIntegralizado.  # noqa: E501
        :type: list[TipoUsinaValorProgramado]
        """

        self._geracoes_programadas = geracoes_programadas

    @property
    def regiao(self):
        """Gets the regiao of this GeracaoProgramadoIntegralizado.  # noqa: E501


        :return: The regiao of this GeracaoProgramadoIntegralizado.  # noqa: E501
        :rtype: str
        """
        return self._regiao

    @regiao.setter
    def regiao(self, regiao):
        """Sets the regiao of this GeracaoProgramadoIntegralizado.


        :param regiao: The regiao of this GeracaoProgramadoIntegralizado.  # noqa: E501
        :type: str
        """
        if regiao is None:
            raise ValueError("Invalid value for `regiao`, must not be `None`")  # noqa: E501
        allowed_values = ["SIN", "N", "NE", "SE", "S"]  # noqa: E501
        if regiao not in allowed_values:
            raise ValueError(
                "Invalid value for `regiao` ({0}), must be one of {1}"  # noqa: E501
                .format(regiao, allowed_values)
            )

        self._regiao = regiao

    @property
    def regiao_descricao(self):
        """Gets the regiao_descricao of this GeracaoProgramadoIntegralizado.  # noqa: E501


        :return: The regiao_descricao of this GeracaoProgramadoIntegralizado.  # noqa: E501
        :rtype: str
        """
        return self._regiao_descricao

    @regiao_descricao.setter
    def regiao_descricao(self, regiao_descricao):
        """Sets the regiao_descricao of this GeracaoProgramadoIntegralizado.


        :param regiao_descricao: The regiao_descricao of this GeracaoProgramadoIntegralizado.  # noqa: E501
        :type: str
        """

        self._regiao_descricao = regiao_descricao

    @property
    def regiao_sigla(self):
        """Gets the regiao_sigla of this GeracaoProgramadoIntegralizado.  # noqa: E501


        :return: The regiao_sigla of this GeracaoProgramadoIntegralizado.  # noqa: E501
        :rtype: str
        """
        return self._regiao_sigla

    @regiao_sigla.setter
    def regiao_sigla(self, regiao_sigla):
        """Sets the regiao_sigla of this GeracaoProgramadoIntegralizado.


        :param regiao_sigla: The regiao_sigla of this GeracaoProgramadoIntegralizado.  # noqa: E501
        :type: str
        """

        self._regiao_sigla = regiao_sigla

    @property
    def ano(self):
        """Gets the ano of this GeracaoProgramadoIntegralizado.  # noqa: E501


        :return: The ano of this GeracaoProgramadoIntegralizado.  # noqa: E501
        :rtype: int
        """
        return self._ano

    @ano.setter
    def ano(self, ano):
        """Sets the ano of this GeracaoProgramadoIntegralizado.


        :param ano: The ano of this GeracaoProgramadoIntegralizado.  # noqa: E501
        :type: int
        """
        if ano is None:
            raise ValueError("Invalid value for `ano`, must not be `None`")  # noqa: E501

        self._ano = ano

    @property
    def mes(self):
        """Gets the mes of this GeracaoProgramadoIntegralizado.  # noqa: E501


        :return: The mes of this GeracaoProgramadoIntegralizado.  # noqa: E501
        :rtype: int
        """
        return self._mes

    @mes.setter
    def mes(self, mes):
        """Sets the mes of this GeracaoProgramadoIntegralizado.


        :param mes: The mes of this GeracaoProgramadoIntegralizado.  # noqa: E501
        :type: int
        """
        if mes is None:
            raise ValueError("Invalid value for `mes`, must not be `None`")  # noqa: E501

        self._mes = mes

    @property
    def dia(self):
        """Gets the dia of this GeracaoProgramadoIntegralizado.  # noqa: E501


        :return: The dia of this GeracaoProgramadoIntegralizado.  # noqa: E501
        :rtype: int
        """
        return self._dia

    @dia.setter
    def dia(self, dia):
        """Sets the dia of this GeracaoProgramadoIntegralizado.


        :param dia: The dia of this GeracaoProgramadoIntegralizado.  # noqa: E501
        :type: int
        """
        if dia is None:
            raise ValueError("Invalid value for `dia`, must not be `None`")  # noqa: E501

        self._dia = dia

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
        if issubclass(GeracaoProgramadoIntegralizado, dict):
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
        if not isinstance(other, GeracaoProgramadoIntegralizado):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other