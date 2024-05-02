# Análise do banco de dados de renda dos clientes.

Entendimento do negócio
  Nesse notebook serão analisados os dados de um banco com informações de de clientes de uma instituição financeira. O objetivo final é prever a renda de clientes, com base nas características. Serão realizadas algumas etapas:
- Carregamento dos dados;
- Estruturação desses dados, corrigindo ausência de valores e outras condições;
- Determinação de modelos estatísticos de Regressão Linear múltipla para predição da renda;
- Análise de qualidade dos modelos;
- Implementação e deploy dos dados;

# Tutorial 1:
https://github.com/gfsilveira/ebac/assets/31182449/c0473f6a-d49e-41f4-8a45-4e0edf8c5921

# Tutorial 2:
https://github.com/gfsilveira/ebac/assets/31182449/152df21d-d7b7-4cfb-95ad-887a44fea565

# Dicionário de Dados


| Variavel                 | Descrição                                             | Tipo      |
|:------------------------:|:-----------------------------------------------------:|:---------:|
|data_ref                  | Data de referência de coleta das variáveis            |datetime   |
|sexo                      | Sexo do cliente                                       |object     |
|posse_de_veiculo          | Indica se o cliente possui veículo                    |bool       |
|posse_de_imovel           | Indica se o cliente possui imóvel                     |bool       |
|qtd_filhos                | Quantidade de filhos do cliente                       |category   |
|tipo_renda                | Tipo de renda do cliente                              |object     |
|educacao                  | Grau de instrução do cliente                          |object     |
|idade                     | Idade do cliente                                      |int64      |
|tempo_emprego             | Tempo no emprego atual                                |float64    |
|qt_pessoas_residencia     | Quantidade de pessoas que moram na residência         |category   |
|renda                     | Renda em reais                                        |float64    |
|renda_media_movel         | Média móvel da Renda em reais                         |float64    |
|tempo_emprego_media_movel | Média móvel da Tempo no emprego atual                 |float64    |
