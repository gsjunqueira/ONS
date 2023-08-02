# RespostaConsultaSituacaoImportacaoLoteDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**processado** | **bool** | Indica que o lote foi processado. | [optional] 
**numero_solicitacao** | **str** | Número da solicitação no SGI. | [optional] 
**data_solicitacao** | **datetime** | Data da solicitação no SGI. | [optional] 
**data_processamento** | **datetime** | Data de processamento de a intervenção tiver sido processada. | [optional] 
**total_registros_validos** | **int** | Total de registros válidos. | [optional] 
**total_registros_invalidos** | **int** | Total de registros inválidos. | [optional] 
**total_intervencoes_agendadas** | **int** | Total de intervenções agendadas para importação. | [optional] 
**ind_erro** | **bool** | Indica a existência de erro na resposta. | 
**mensagem_erro** | [**MensagemErroDto**](MensagemErroDto.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

