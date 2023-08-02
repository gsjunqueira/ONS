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

class Empresa(object):
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
        'codigo': 'str',
        'nome': 'str',
        'sigla': 'str',
        'bdt_id': 'str',
        'regiao': 'str',
        'regiao_descricao': 'str',
        'regiao_sigla': 'str'
    }

    attribute_map = {
        'codigo': 'Codigo',
        'nome': 'Nome',
        'sigla': 'Sigla',
        'bdt_id': 'BDT_Id',
        'regiao': 'Regiao',
        'regiao_descricao': 'RegiaoDescricao',
        'regiao_sigla': 'RegiaoSigla'
    }

    def __init__(self, codigo=None, nome=None, sigla=None, bdt_id=None, regiao=None, regiao_descricao=None, regiao_sigla=None):  # noqa: E501
        """Empresa - a model defined in Swagger"""  # noqa: E501
        self._codigo = None
        self._nome = None
        self._sigla = None
        self._bdt_id = None
        self._regiao = None
        self._regiao_descricao = None
        self._regiao_sigla = None
        self.discriminator = None
        self.codigo = codigo
        self.nome = nome
        self.sigla = sigla
        self.bdt_id = bdt_id
        if regiao is not None:
            self.regiao = regiao
        if regiao_descricao is not None:
            self.regiao_descricao = regiao_descricao
        if regiao_sigla is not None:
            self.regiao_sigla = regiao_sigla

    @property
    def codigo(self):
        """Gets the codigo of this Empresa.  # noqa: E501


        :return: The codigo of this Empresa.  # noqa: E501
        :rtype: str
        """
        return self._codigo

    @codigo.setter
    def codigo(self, codigo):
        """Sets the codigo of this Empresa.


        :param codigo: The codigo of this Empresa.  # noqa: E501
        :type: str
        """
        if codigo is None:
            raise ValueError("Invalid value for `codigo`, must not be `None`")  # noqa: E501

        self._codigo = codigo

    @property
    def nome(self):
        """Gets the nome of this Empresa.  # noqa: E501


        :return: The nome of this Empresa.  # noqa: E501
        :rtype: str
        """
        return self._nome

    @nome.setter
    def nome(self, nome):
        """Sets the nome of this Empresa.


        :param nome: The nome of this Empresa.  # noqa: E501
        :type: str
        """
        if nome is None:
            raise ValueError("Invalid value for `nome`, must not be `None`")  # noqa: E501

        self._nome = nome

    @property
    def sigla(self):
        """Gets the sigla of this Empresa.  # noqa: E501


        :return: The sigla of this Empresa.  # noqa: E501
        :rtype: str
        """
        return self._sigla

    @sigla.setter
    def sigla(self, sigla):
        """Sets the sigla of this Empresa.


        :param sigla: The sigla of this Empresa.  # noqa: E501
        :type: str
        """
        if sigla is None:
            raise ValueError("Invalid value for `sigla`, must not be `None`")  # noqa: E501

        self._sigla = sigla

    @property
    def bdt_id(self):
        """Gets the bdt_id of this Empresa.  # noqa: E501


        :return: The bdt_id of this Empresa.  # noqa: E501
        :rtype: str
        """
        return self._bdt_id

    @bdt_id.setter
    def bdt_id(self, bdt_id):
        """Sets the bdt_id of this Empresa.


        :param bdt_id: The bdt_id of this Empresa.  # noqa: E501
        :type: str
        """
        if bdt_id is None:
            raise ValueError("Invalid value for `bdt_id`, must not be `None`")  # noqa: E501

        self._bdt_id = bdt_id

    @property
    def regiao(self):
        """Gets the regiao of this Empresa.  # noqa: E501


        :return: The regiao of this Empresa.  # noqa: E501
        :rtype: str
        """
        return self._regiao

    @regiao.setter
    def regiao(self, regiao):
        """Sets the regiao of this Empresa.


        :param regiao: The regiao of this Empresa.  # noqa: E501
        :type: str
        """
        allowed_values = ["SIN", "N", "NE", "SE", "S"]  # noqa: E501
        if regiao not in allowed_values:
            raise ValueError(
                "Invalid value for `regiao` ({0}), must be one of {1}"  # noqa: E501
                .format(regiao, allowed_values)
            )

        self._regiao = regiao

    @property
    def regiao_descricao(self):
        """Gets the regiao_descricao of this Empresa.  # noqa: E501


        :return: The regiao_descricao of this Empresa.  # noqa: E501
        :rtype: str
        """
        return self._regiao_descricao

    @regiao_descricao.setter
    def regiao_descricao(self, regiao_descricao):
        """Sets the regiao_descricao of this Empresa.


        :param regiao_descricao: The regiao_descricao of this Empresa.  # noqa: E501
        :type: str
        """

        self._regiao_descricao = regiao_descricao

    @property
    def regiao_sigla(self):
        """Gets the regiao_sigla of this Empresa.  # noqa: E501


        :return: The regiao_sigla of this Empresa.  # noqa: E501
        :rtype: str
        """
        return self._regiao_sigla

    @regiao_sigla.setter
    def regiao_sigla(self, regiao_sigla):
        """Sets the regiao_sigla of this Empresa.


        :param regiao_sigla: The regiao_sigla of this Empresa.  # noqa: E501
        :type: str
        """

        self._regiao_sigla = regiao_sigla

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
        if issubclass(Empresa, dict):
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
        if not isinstance(other, Empresa):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other