# IntervencaoDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**numero_ons** | **str** | Número da intervenção no ONS. | [optional] 
**numero_agente** | **str** | Número do agente. | [optional] 
**data_hora_solicitacao** | **datetime** | Data e hora da solicitação. | [optional] 
**situacao** | **str** | Situação da intervenção. | [optional] 
**nome_centro_responsavel** | **str** | Nome do centro responsa´vel. | [optional] 
**nome_agente_solicitante** | **str** | Nome do agente solicitante. | [optional] 
**nome_agente_responsavel** | **str** | Nome do agente responsável. | [optional] 
**malha** | **str** | Malha associada a intervenção. | [optional] 
**servicos** | **str** | Serviços. | [optional] 
**observacoes** | **str** | Observações. | [optional] 
**equipamentos** | [**list[EquipamentoIntervencaoDto]**](EquipamentoIntervencaoDto.md) | Equipamentos associados a intervenção. | [optional] 
**data_hora_inicio** | **datetime** | Data e hora de início. | [optional] 
**data_hora_fim** | **datetime** | Data e hora fim. | [optional] 
**periodicidade** | **str** | Periodicidade. | [optional] 
**natureza** | **str** | Natureza. | [optional] 
**classificacao** | **str** | Classificação. | [optional] 
**justificativa_fora_prazo** | **str** | Justificativa fora do prazo. | [optional] 
**tipo** | **int** | Tipo. | [optional] 
**caracterizacao** | **str** | Caracterização. | [optional] 
**intervencao_aproveitamento** | **str** | Intervenção do aproveitamento. | [optional] 
**intervencao_inclusao_servico** | **str** | Intervenção de inclusão de serviço. | [optional] 
**intervencao_suspensa_ons** | **str** | Intervenção suspensa ONS. | [optional] 
**elevado_risco_desligamento** | **str** | Elevado risco de desligamento. | [optional] 
**depende_condicoes_climaticas** | **str** | Depende de condições climáticas. | [optional] 
**execucao_periodo_noturno** | **str** | Execução no período noturno. | [optional] 
**postergacao_traz_risco** | **bool** | Postageração traz risco de desligamento. | [optional] 
**acarreta_perdas_multiplas** | **bool** | Acarreta múltiplias perdas. | [optional] 
**envolve_rele_protecao** | **bool** | Envolve relê de proteção. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

