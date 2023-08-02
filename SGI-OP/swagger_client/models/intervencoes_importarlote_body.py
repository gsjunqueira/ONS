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

class IntervencoesImportarloteBody(object):
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
        'anexo9': 'str',
        'anexo10': 'str',
        'anexo2': 'str',
        'arquivo_dados': 'str',
        'anexo8': 'str',
        'anexo4': 'str',
        'anexo5': 'str',
        'anexo3': 'str',
        'anexo6': 'str',
        'anexo7': 'str',
        'anexo1': 'str'
    }

    attribute_map = {
        'anexo9': 'anexo9',
        'anexo10': 'anexo10',
        'anexo2': 'anexo2',
        'arquivo_dados': 'arquivoDados',
        'anexo8': 'anexo8',
        'anexo4': 'anexo4',
        'anexo5': 'anexo5',
        'anexo3': 'anexo3',
        'anexo6': 'anexo6',
        'anexo7': 'anexo7',
        'anexo1': 'anexo1'
    }

    def __init__(self, anexo9=None, anexo10=None, anexo2=None, arquivo_dados=None, anexo8=None, anexo4=None, anexo5=None, anexo3=None, anexo6=None, anexo7=None, anexo1=None):  # noqa: E501
        """IntervencoesImportarloteBody - a model defined in Swagger"""  # noqa: E501
        self._anexo9 = None
        self._anexo10 = None
        self._anexo2 = None
        self._arquivo_dados = None
        self._anexo8 = None
        self._anexo4 = None
        self._anexo5 = None
        self._anexo3 = None
        self._anexo6 = None
        self._anexo7 = None
        self._anexo1 = None
        self.discriminator = None
        if anexo9 is not None:
            self.anexo9 = anexo9
        if anexo10 is not None:
            self.anexo10 = anexo10
        if anexo2 is not None:
            self.anexo2 = anexo2
        self.arquivo_dados = arquivo_dados
        if anexo8 is not None:
            self.anexo8 = anexo8
        if anexo4 is not None:
            self.anexo4 = anexo4
        if anexo5 is not None:
            self.anexo5 = anexo5
        if anexo3 is not None:
            self.anexo3 = anexo3
        if anexo6 is not None:
            self.anexo6 = anexo6
        if anexo7 is not None:
            self.anexo7 = anexo7
        if anexo1 is not None:
            self.anexo1 = anexo1

    @property
    def anexo9(self):
        """Gets the anexo9 of this IntervencoesImportarloteBody.  # noqa: E501

        Arquivo Anexo a intervenção  # noqa: E501

        :return: The anexo9 of this IntervencoesImportarloteBody.  # noqa: E501
        :rtype: str
        """
        return self._anexo9

    @anexo9.setter
    def anexo9(self, anexo9):
        """Sets the anexo9 of this IntervencoesImportarloteBody.

        Arquivo Anexo a intervenção  # noqa: E501

        :param anexo9: The anexo9 of this IntervencoesImportarloteBody.  # noqa: E501
        :type: str
        """

        self._anexo9 = anexo9

    @property
    def anexo10(self):
        """Gets the anexo10 of this IntervencoesImportarloteBody.  # noqa: E501

        Arquivo Anexo a intervenção  # noqa: E501

        :return: The anexo10 of this IntervencoesImportarloteBody.  # noqa: E501
        :rtype: str
        """
        return self._anexo10

    @anexo10.setter
    def anexo10(self, anexo10):
        """Sets the anexo10 of this IntervencoesImportarloteBody.

        Arquivo Anexo a intervenção  # noqa: E501

        :param anexo10: The anexo10 of this IntervencoesImportarloteBody.  # noqa: E501
        :type: str
        """

        self._anexo10 = anexo10

    @property
    def anexo2(self):
        """Gets the anexo2 of this IntervencoesImportarloteBody.  # noqa: E501

        Arquivo Anexo a intervenção  # noqa: E501

        :return: The anexo2 of this IntervencoesImportarloteBody.  # noqa: E501
        :rtype: str
        """
        return self._anexo2

    @anexo2.setter
    def anexo2(self, anexo2):
        """Sets the anexo2 of this IntervencoesImportarloteBody.

        Arquivo Anexo a intervenção  # noqa: E501

        :param anexo2: The anexo2 of this IntervencoesImportarloteBody.  # noqa: E501
        :type: str
        """

        self._anexo2 = anexo2

    @property
    def arquivo_dados(self):
        """Gets the arquivo_dados of this IntervencoesImportarloteBody.  # noqa: E501

        Arquivo de Dados  # noqa: E501

        :return: The arquivo_dados of this IntervencoesImportarloteBody.  # noqa: E501
        :rtype: str
        """
        return self._arquivo_dados

    @arquivo_dados.setter
    def arquivo_dados(self, arquivo_dados):
        """Sets the arquivo_dados of this IntervencoesImportarloteBody.

        Arquivo de Dados  # noqa: E501

        :param arquivo_dados: The arquivo_dados of this IntervencoesImportarloteBody.  # noqa: E501
        :type: str
        """
        if arquivo_dados is None:
            raise ValueError("Invalid value for `arquivo_dados`, must not be `None`")  # noqa: E501

        self._arquivo_dados = arquivo_dados

    @property
    def anexo8(self):
        """Gets the anexo8 of this IntervencoesImportarloteBody.  # noqa: E501

        Arquivo Anexo a intervenção  # noqa: E501

        :return: The anexo8 of this IntervencoesImportarloteBody.  # noqa: E501
        :rtype: str
        """
        return self._anexo8

    @anexo8.setter
    def anexo8(self, anexo8):
        """Sets the anexo8 of this IntervencoesImportarloteBody.

        Arquivo Anexo a intervenção  # noqa: E501

        :param anexo8: The anexo8 of this IntervencoesImportarloteBody.  # noqa: E501
        :type: str
        """

        self._anexo8 = anexo8

    @property
    def anexo4(self):
        """Gets the anexo4 of this IntervencoesImportarloteBody.  # noqa: E501

        Arquivo Anexo a intervenção  # noqa: E501

        :return: The anexo4 of this IntervencoesImportarloteBody.  # noqa: E501
        :rtype: str
        """
        return self._anexo4

    @anexo4.setter
    def anexo4(self, anexo4):
        """Sets the anexo4 of this IntervencoesImportarloteBody.

        Arquivo Anexo a intervenção  # noqa: E501

        :param anexo4: The anexo4 of this IntervencoesImportarloteBody.  # noqa: E501
        :type: str
        """

        self._anexo4 = anexo4

    @property
    def anexo5(self):
        """Gets the anexo5 of this IntervencoesImportarloteBody.  # noqa: E501

        Arquivo Anexo a intervenção  # noqa: E501

        :return: The anexo5 of this IntervencoesImportarloteBody.  # noqa: E501
        :rtype: str
        """
        return self._anexo5

    @anexo5.setter
    def anexo5(self, anexo5):
        """Sets the anexo5 of this IntervencoesImportarloteBody.

        Arquivo Anexo a intervenção  # noqa: E501

        :param anexo5: The anexo5 of this IntervencoesImportarloteBody.  # noqa: E501
        :type: str
        """

        self._anexo5 = anexo5

    @property
    def anexo3(self):
        """Gets the anexo3 of this IntervencoesImportarloteBody.  # noqa: E501

        Arquivo Anexo a intervenção  # noqa: E501

        :return: The anexo3 of this IntervencoesImportarloteBody.  # noqa: E501
        :rtype: str
        """
        return self._anexo3

    @anexo3.setter
    def anexo3(self, anexo3):
        """Sets the anexo3 of this IntervencoesImportarloteBody.

        Arquivo Anexo a intervenção  # noqa: E501

        :param anexo3: The anexo3 of this IntervencoesImportarloteBody.  # noqa: E501
        :type: str
        """

        self._anexo3 = anexo3

    @property
    def anexo6(self):
        """Gets the anexo6 of this IntervencoesImportarloteBody.  # noqa: E501

        Arquivo Anexo a intervenção  # noqa: E501

        :return: The anexo6 of this IntervencoesImportarloteBody.  # noqa: E501
        :rtype: str
        """
        return self._anexo6

    @anexo6.setter
    def anexo6(self, anexo6):
        """Sets the anexo6 of this IntervencoesImportarloteBody.

        Arquivo Anexo a intervenção  # noqa: E501

        :param anexo6: The anexo6 of this IntervencoesImportarloteBody.  # noqa: E501
        :type: str
        """

        self._anexo6 = anexo6

    @property
    def anexo7(self):
        """Gets the anexo7 of this IntervencoesImportarloteBody.  # noqa: E501

        Arquivo Anexo a intervenção  # noqa: E501

        :return: The anexo7 of this IntervencoesImportarloteBody.  # noqa: E501
        :rtype: str
        """
        return self._anexo7

    @anexo7.setter
    def anexo7(self, anexo7):
        """Sets the anexo7 of this IntervencoesImportarloteBody.

        Arquivo Anexo a intervenção  # noqa: E501

        :param anexo7: The anexo7 of this IntervencoesImportarloteBody.  # noqa: E501
        :type: str
        """

        self._anexo7 = anexo7

    @property
    def anexo1(self):
        """Gets the anexo1 of this IntervencoesImportarloteBody.  # noqa: E501

        Arquivo Anexo a intervenção  # noqa: E501

        :return: The anexo1 of this IntervencoesImportarloteBody.  # noqa: E501
        :rtype: str
        """
        return self._anexo1

    @anexo1.setter
    def anexo1(self, anexo1):
        """Sets the anexo1 of this IntervencoesImportarloteBody.

        Arquivo Anexo a intervenção  # noqa: E501

        :param anexo1: The anexo1 of this IntervencoesImportarloteBody.  # noqa: E501
        :type: str
        """

        self._anexo1 = anexo1

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
        if issubclass(IntervencoesImportarloteBody, dict):
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
        if not isinstance(other, IntervencoesImportarloteBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
