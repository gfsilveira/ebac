# Importando bibliotecas
import pandas as pd               # Gerenciamento e análise dos bancos de dados
import matplotlib.pyplot as plt   # Plotagem e salvamento dos gráfico
import streamlit as st


def __grafico(
    df: pd.DataFrame,
    values: str|list,
    index: str|list,
    aggfunc: str,
    tipo: str,
    title: str,
    xlabel: str,
    ylabel: str,
  ) -> None:
  '''
    Salvamento dos gráficos.
    :param fig_name (str): Nome do gráfico com caminho de diretórios.
    :param df (pd.DataFrame): Conjunto de dados para o plot.
    :param values (str|list): Valores (colunas) agrupados pelo pivot_table.
    :param index (str|list): Index (indice) agrupados pelo pivot_table.
    :param aggfunc (str): Função de agregação do pivot_table.
    :param tipo (str): Gráfico pivot_table sem função adicional `nada`,
                        `unstack` ou `sort_values`.
    :param title (str): Título do gráfico.
    :param xlabel (str): Leganda do eixo x.
    :param ylabel (str): Leganda do eixo y.
  '''
  match tipo:
    case "nada":
      grahic_1 = pd.pivot_table(
                              df,
                              values=values,
                              index=index,
                              aggfunc=aggfunc
                            )
    case "unstack":
      grahic_1 = pd.pivot_table(
                              df,
                              values=values,
                              index=index,
                              aggfunc=aggfunc
                            ).unstack()
    case "sort_values":
      grahic_1 = pd.pivot_table(
                              df,
                              values=values,
                              index=index,
                              aggfunc=aggfunc
                            ).sort_values(values)
    case _:
      print("Opção de gráfico inválida inválida")
      return None

  figsize = (18,5)
  grahic_1.plot(figsize=figsize)
  plt.title(title, size=18)
  plt.xlabel(xlabel, size=14)
  plt.ylabel(ylabel, size=14)
  st.pyplot(fig=plt)

  return None


def gera_graficos(df: pd.DataFrame) -> None:
  '''
  Função geradora de gráficos mensais para os reltórios solicitados
  :param mes (int): Número correspondente do mês de interesse. Caso não seja
                    passado nenhum valor, os gráficos serão gerados para o mês
                    anterior ao atual.
  '''
  try:
    # Plotando o primeiro gráfico
    pr_gf = {
                  "df": df,
                  "values": "IDADEMAE",
                  "index": "DTNASC",
                  "aggfunc": "mean",
                  "tipo": "nada",
                  "title": f"Média da idade das Mães",
                  "xlabel": "Data do Parto",
                  "ylabel": "Média da Idade das Mães no Parto",

    }
    __grafico(**pr_gf)
  except:
    print("Gráfico de média das idades das mães não foi obtido")
    return None

  try:
    # Plotando o segundo gráfico
    pr_gf["aggfunc"] = "count"
    pr_gf["title"] = f"Número de nascimentos"
    pr_gf["ylabel"] = "Número de nascidos"

    __grafico(**pr_gf)
  except:
    print("Gráfico de número de nascidos não foi obtido")
    return None

  try:
    # Plotando o terceiro gráfico
    pr_gf["index"] = ["DTNASC","SEXO"]
    pr_gf["tipo"] = "unstack"
    pr_gf["title"] = f"Número de nascimentos por sexo"

    __grafico(**pr_gf)
  except:
    print("Gráfico de número de nascidos por sexo não foi obtido")
    return None

  try:
    # Plotando o quarto gráfico
    pr_gf["values"] = "PESO"
    pr_gf["ylabel"] = "Peso médio"
    pr_gf["title"] = f"Média de peso de bebês por sexo"
    pr_gf["aggfunc"] = "mean"

    __grafico(**pr_gf)
  except:
    print("Gráfico de média de peso por sexo não foi obtido")
    return None

  try:
    # Plotando o quinto gráfico
    pr_gf["index"] = "ESCMAE"
    pr_gf["aggfunc"] = "median"
    pr_gf["tipo"] = "sort_values"
    pr_gf["title"] = f"Média de Peso dos bebês pela escolaridade da Mãe"
    pr_gf["xlabel"] = "Escolaridade da Mãe"

    __grafico(**pr_gf)
  except:
    print("Gráfico de peso por escolaridade da mãe não foi obtido")
    return None

  try:
    # Plotando o sexto gráfico
    pr_gf["values"] = "APGAR1"
    pr_gf["index"] = "GESTACAO"
    pr_gf["aggfunc"] = "mean"
    pr_gf["title"] = f"Média do APGAR1 por semanas de gestação"
    pr_gf["xlabel"] = "Semanas de Gestação"
    pr_gf["ylabel"] = "APGAR1"

    __grafico(**pr_gf)
  except:
    print("Gráfico de APGAR1 por gestação não foi obtido")
    return None

  try:
    # Plotando o sétimo gráfico
    pr_gf["values"] = "APGAR5"
    pr_gf["title"] = f"Média do APGAR5 por semanas de gestação"
    pr_gf["ylabel"] = "APGAR5"

    __grafico(**pr_gf)
  except:
    print("Gráfico de APGAR5 por gestação não foi obtido")
    return None