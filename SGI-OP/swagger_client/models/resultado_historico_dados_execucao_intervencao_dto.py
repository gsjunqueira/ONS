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

class ResultadoHistoricoDadosExecucaoIntervencaoDto(object):
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
        'identificador_ons': 'str',
        'historico': 'list[HistoricoDto]',
        'dados_execucao': 'list[DadosExecucaoDto]',
        'ind_erro': 'bool',
        'mensagem_erro': 'MensagemErroDto'
    }

    attribute_map = {
        'identificador_ons': 'identificadorONS',
        'historico': 'historico',
        'dados_execucao': 'dadosExecucao',
        'ind_erro': 'indErro',
        'mensagem_erro': 'mensagemErro'
    }

    def __init__(self, identificador_ons=None, historico=None, dados_execucao=None, ind_erro=None, mensagem_erro=None):  # noqa: E501
        """ResultadoHistoricoDadosExecucaoIntervencaoDto - a model defined in Swagger"""  # noqa: E501
        self._identificador_ons = None
        self._historico = None
        self._dados_execucao = None
        self._ind_erro = None
        self._mensagem_erro = None
        self.discriminator = None
        if identificador_ons is not None:
            self.identificador_ons = identificador_ons
        if historico is not None:
            self.historico = historico
        if dados_execucao is not None:
            self.dados_execucao = dados_execucao
        self.ind_erro = ind_erro
        if mensagem_erro is not None:
            self.mensagem_erro = mensagem_erro

    @property
    def identificador_ons(self):
        """Gets the identificador_ons of this ResultadoHistoricoDadosExecucaoIntervencaoDto.  # noqa: E501

        Identificador ONS  # noqa: E501

        :return: The identificador_ons of this ResultadoHistoricoDadosExecucaoIntervencaoDto.  # noqa: E501
        :rtype: str
        """
        return self._identificador_ons

    @identificador_ons.setter
    def identificador_ons(self, identificador_ons):
        """Sets the identificador_ons of this ResultadoHistoricoDadosExecucaoIntervencaoDto.

        Identificador ONS  # noqa: E501

        :param identificador_ons: The identificador_ons of this ResultadoHistoricoDadosExecucaoIntervencaoDto.  # noqa: E501
        :type: str
        """

        self._identificador_ons = identificador_ons

    @property
    def historico(self):
        """Gets the historico of this ResultadoHistoricoDadosExecucaoIntervencaoDto.  # noqa: E501

        historico da intervenção  # noqa: E501

        :return: The historico of this ResultadoHistoricoDadosExecucaoIntervencaoDto.  # noqa: E501
        :rtype: list[HistoricoDto]
        """
        return self._historico

    @historico.setter
    def historico(self, historico):
        """Sets the historico of this ResultadoHistoricoDadosExecucaoIntervencaoDto.

        historico da intervenção  # noqa: E501

        :param historico: The historico of this ResultadoHistoricoDadosExecucaoIntervencaoDto.  # noqa: E501
        :type: list[HistoricoDto]
        """

        self._historico = historico

    @property
    def dados_execucao(self):
        """Gets the dados_execucao of this ResultadoHistoricoDadosExecucaoIntervencaoDto.  # noqa: E501

        Dados de Execucao da intervenção  # noqa: E501

        :return: The dados_execucao of this ResultadoHistoricoDadosExecucaoIntervencaoDto.  # noqa: E501
        :rtype: list[DadosExecucaoDto]
        """
        return self._dados_execucao

    @dados_execucao.setter
    def dados_execucao(self, dados_execucao):
        """Sets the dados_execucao of this ResultadoHistoricoDadosExecucaoIntervencaoDto.

        Dados de Execucao da intervenção  # noqa: E501

        :param dados_execucao: The dados_execucao of this ResultadoHistoricoDadosExecucaoIntervencaoDto.  # noqa: E501
        :type: list[DadosExecucaoDto]
        """

        self._dados_execucao = dados_execucao

    @property
    def ind_erro(self):
        """Gets the ind_erro of this ResultadoHistoricoDadosExecucaoIntervencaoDto.  # noqa: E501

        Indica a existência de erro na resposta.  # noqa: E501

        :return: The ind_erro of this ResultadoHistoricoDadosExecucaoIntervencaoDto.  # noqa: E501
        :rtype: bool
        """
        return self._ind_erro

    @ind_erro.setter
    def ind_erro(self, ind_erro):
        """Sets the ind_erro of this ResultadoHistoricoDadosExecucaoIntervencaoDto.

        Indica a existência de erro na resposta.  # noqa: E501

        :param ind_erro: The ind_erro of this ResultadoHistoricoDadosExecucaoIntervencaoDto.  # noqa: E501
        :type: bool
        """
        if ind_erro is None:
            raise ValueError("Invalid value for `ind_erro`, must not be `None`")  # noqa: E501

        self._ind_erro = ind_erro

    @property
    def mensagem_erro(self):
        """Gets the mensagem_erro of this ResultadoHistoricoDadosExecucaoIntervencaoDto.  # noqa: E501


        :return: The mensagem_erro of this ResultadoHistoricoDadosExecucaoIntervencaoDto.  # noqa: E501
        :rtype: MensagemErroDto
        """
        return self._mensagem_erro

    @mensagem_erro.setter
    def mensagem_erro(self, mensagem_erro):
        """Sets the mensagem_erro of this ResultadoHistoricoDadosExecucaoIntervencaoDto.


        :param mensagem_erro: The mensagem_erro of this ResultadoHistoricoDadosExecucaoIntervencaoDto.  # noqa: E501
        :type: MensagemErroDto
        """

        self._mensagem_erro = mensagem_erro

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
        if issubclass(ResultadoHistoricoDadosExecucaoIntervencaoDto, dict):
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
        if not isinstance(other, ResultadoHistoricoDadosExecucaoIntervencaoDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
