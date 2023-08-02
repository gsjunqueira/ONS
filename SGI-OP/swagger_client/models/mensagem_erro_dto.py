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

class MensagemErroDto(object):
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
        'mensagem': 'str'
    }

    attribute_map = {
        'codigo': 'Codigo',
        'mensagem': 'Mensagem'
    }

    def __init__(self, codigo=None, mensagem=None):  # noqa: E501
        """MensagemErroDto - a model defined in Swagger"""  # noqa: E501
        self._codigo = None
        self._mensagem = None
        self.discriminator = None
        self.codigo = codigo
        self.mensagem = mensagem

    @property
    def codigo(self):
        """Gets the codigo of this MensagemErroDto.  # noqa: E501

        Código da resposta.  # noqa: E501

        :return: The codigo of this MensagemErroDto.  # noqa: E501
        :rtype: str
        """
        return self._codigo

    @codigo.setter
    def codigo(self, codigo):
        """Sets the codigo of this MensagemErroDto.

        Código da resposta.  # noqa: E501

        :param codigo: The codigo of this MensagemErroDto.  # noqa: E501
        :type: str
        """
        if codigo is None:
            raise ValueError("Invalid value for `codigo`, must not be `None`")  # noqa: E501

        self._codigo = codigo

    @property
    def mensagem(self):
        """Gets the mensagem of this MensagemErroDto.  # noqa: E501

        Mensagem da resposta.  # noqa: E501

        :return: The mensagem of this MensagemErroDto.  # noqa: E501
        :rtype: str
        """
        return self._mensagem

    @mensagem.setter
    def mensagem(self, mensagem):
        """Sets the mensagem of this MensagemErroDto.

        Mensagem da resposta.  # noqa: E501

        :param mensagem: The mensagem of this MensagemErroDto.  # noqa: E501
        :type: str
        """
        if mensagem is None:
            raise ValueError("Invalid value for `mensagem`, must not be `None`")  # noqa: E501

        self._mensagem = mensagem

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
        if issubclass(MensagemErroDto, dict):
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
        if not isinstance(other, MensagemErroDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other