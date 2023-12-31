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

class GeracaoPropostaGETResponse(object):
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
        'usinas': 'list[Usina]',
        'page': 'int',
        'page_size': 'int',
        'total': 'int',
        'inicio_processamento': 'datetime',
        'termino_processamento': 'datetime'
    }

    attribute_map = {
        'usinas': 'Usinas',
        'page': 'Page',
        'page_size': 'PageSize',
        'total': 'Total',
        'inicio_processamento': 'InicioProcessamento',
        'termino_processamento': 'TerminoProcessamento'
    }

    def __init__(self, usinas=None, page=None, page_size=None, total=None, inicio_processamento=None, termino_processamento=None):  # noqa: E501
        """GeracaoPropostaGETResponse - a model defined in Swagger"""  # noqa: E501
        self._usinas = None
        self._page = None
        self._page_size = None
        self._total = None
        self._inicio_processamento = None
        self._termino_processamento = None
        self.discriminator = None
        self.usinas = usinas
        if page is not None:
            self.page = page
        if page_size is not None:
            self.page_size = page_size
        if total is not None:
            self.total = total
        self.inicio_processamento = inicio_processamento
        self.termino_processamento = termino_processamento

    @property
    def usinas(self):
        """Gets the usinas of this GeracaoPropostaGETResponse.  # noqa: E501

        Lista de Usinas da Empresa  # noqa: E501

        :return: The usinas of this GeracaoPropostaGETResponse.  # noqa: E501
        :rtype: list[Usina]
        """
        return self._usinas

    @usinas.setter
    def usinas(self, usinas):
        """Sets the usinas of this GeracaoPropostaGETResponse.

        Lista de Usinas da Empresa  # noqa: E501

        :param usinas: The usinas of this GeracaoPropostaGETResponse.  # noqa: E501
        :type: list[Usina]
        """
        if usinas is None:
            raise ValueError("Invalid value for `usinas`, must not be `None`")  # noqa: E501

        self._usinas = usinas

    @property
    def page(self):
        """Gets the page of this GeracaoPropostaGETResponse.  # noqa: E501


        :return: The page of this GeracaoPropostaGETResponse.  # noqa: E501
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this GeracaoPropostaGETResponse.


        :param page: The page of this GeracaoPropostaGETResponse.  # noqa: E501
        :type: int
        """

        self._page = page

    @property
    def page_size(self):
        """Gets the page_size of this GeracaoPropostaGETResponse.  # noqa: E501


        :return: The page_size of this GeracaoPropostaGETResponse.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this GeracaoPropostaGETResponse.


        :param page_size: The page_size of this GeracaoPropostaGETResponse.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def total(self):
        """Gets the total of this GeracaoPropostaGETResponse.  # noqa: E501


        :return: The total of this GeracaoPropostaGETResponse.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this GeracaoPropostaGETResponse.


        :param total: The total of this GeracaoPropostaGETResponse.  # noqa: E501
        :type: int
        """

        self._total = total

    @property
    def inicio_processamento(self):
        """Gets the inicio_processamento of this GeracaoPropostaGETResponse.  # noqa: E501

        Momento em que iniciou o processamento de uma requisição.  # noqa: E501

        :return: The inicio_processamento of this GeracaoPropostaGETResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._inicio_processamento

    @inicio_processamento.setter
    def inicio_processamento(self, inicio_processamento):
        """Sets the inicio_processamento of this GeracaoPropostaGETResponse.

        Momento em que iniciou o processamento de uma requisição.  # noqa: E501

        :param inicio_processamento: The inicio_processamento of this GeracaoPropostaGETResponse.  # noqa: E501
        :type: datetime
        """
        if inicio_processamento is None:
            raise ValueError("Invalid value for `inicio_processamento`, must not be `None`")  # noqa: E501

        self._inicio_processamento = inicio_processamento

    @property
    def termino_processamento(self):
        """Gets the termino_processamento of this GeracaoPropostaGETResponse.  # noqa: E501

        Momento de término de processamento de uma requisição.  # noqa: E501

        :return: The termino_processamento of this GeracaoPropostaGETResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._termino_processamento

    @termino_processamento.setter
    def termino_processamento(self, termino_processamento):
        """Sets the termino_processamento of this GeracaoPropostaGETResponse.

        Momento de término de processamento de uma requisição.  # noqa: E501

        :param termino_processamento: The termino_processamento of this GeracaoPropostaGETResponse.  # noqa: E501
        :type: datetime
        """
        if termino_processamento is None:
            raise ValueError("Invalid value for `termino_processamento`, must not be `None`")  # noqa: E501

        self._termino_processamento = termino_processamento

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
        if issubclass(GeracaoPropostaGETResponse, dict):
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
        if not isinstance(other, GeracaoPropostaGETResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
