# Importando bibliotecas
import os                         # Acesso as informações do SO
import pandas as pd               # Gerenciamento e análise dos bancos de dados
import matplotlib.pyplot as plt   # Plotagem e salvamento dos gráfico
plt.ioff()                        # Suprime a demonstração dos gráficos
from datetime import date         # Trabalha com datas


def __grafico(
    fig_name: str,
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
  plt.title(title)
  plt.xlabel(xlabel)
  plt.ylabel(ylabel)
  plt.savefig(fig_name, bbox_inches='tight')
  plt.close()

  return None


def gera_graficos(mes: int = -1) -> None:
  '''
  Função geradora de gráficos mensais para os reltórios solicitados
  :param mes (int): Número correspondente do mês de interesse. Caso não seja
                    passado nenhum valor, os gráficos serão gerados para o mês
                    anterior ao atual.
  '''
  # Meses do ano.
  meses = ["Janeiro",
          "Fevereiro",
          "Março",
          "Abril",
          "Maio",
          "Junho",
          "Julho",
          "Agosto",
          "Setembro",
          "Outubro",
          "Novembro",
          "Dezembro"]
  try:
    # Selecionando o caminho dos dados
    if mes == -1:
      mes = date.today().month - 1

    mes = meses[mes]
    link = "https://raw.githubusercontent.com/gfsilveira/ebac/main/"
    link += "03-Cientista%20de%20Dados/02-Crisp-DM/M%C3%B3dulo_14/"
    link += f"input/SINASC_RO_2019_{mes[:3].upper()}.csv"

    # Lendo arquivo com os dados
    df = pd.read_csv(link)
  except:
    print(f"Dados não encontraddos para mes {mes}")
    return None

  try:
    # Determinando local de persistência
    fig_dir = f"./data/output/figs/{df.DTNASC.max()[:-3]}/"
    os.makedirs(fig_dir, exist_ok=True)
  except:
    print("Local para persistência dos gráficos não encontrado")
    return None

  try:
    # Plotando o primeiro gráfico
    dados = f" (dados de {mes})"
    pr_gf = {
                  "fig_name": fig_dir+"01-IDADE_MAES.png",
                  "df": df,
                  "values": "IDADEMAE",
                  "index": "DTNASC",
                  "aggfunc": "mean",
                  "tipo": "nada",
                  "title": f"Média da idade das Mães{dados}",
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
    pr_gf["title"] = f"Número de nascimentos{dados}"
    pr_gf["ylabel"] = "Número de nascidos"
    pr_gf["fig_name"] = fig_dir+"02-NUM_NASC.png"

    __grafico(**pr_gf)
  except:
    print("Gráfico de número de nascidos não foi obtido")
    return None

  try:
    # Plotando o terceiro gráfico
    pr_gf["index"] = ["DTNASC","SEXO"]
    pr_gf["tipo"] = "unstack"
    pr_gf["title"] = f"Número de nascimentos por sexo{dados}"
    pr_gf["fig_name"] = fig_dir+"03-NUM_NASC_SEXO.png"

    __grafico(**pr_gf)
  except:
    print("Gráfico de número de nascidos por sexo não foi obtido")
    return None

  try:
    # Plotando o quarto gráfico
    pr_gf["values"] = "PESO"
    pr_gf["ylabel"] = "Peso médio"
    pr_gf["title"] = f"Média de peso de bebês por sexo{dados}"
    pr_gf["aggfunc"] = "mean"
    pr_gf["fig_name"] = fig_dir+"04-MEDIA_PESO_SEXO.png"

    __grafico(**pr_gf)
  except:
    print("Gráfico de média de peso por sexo não foi obtido")
    return None

  try:
    # Plotando o quinto gráfico
    pr_gf["index"] = "ESCMAE"
    pr_gf["aggfunc"] = "median"
    pr_gf["tipo"] = "sort_values"
    pr_gf["title"] = f"Média de Peso dos bebês pela escolaridade da Mãe{dados}"
    pr_gf["xlabel"] = "Escolaridade da Mãe"
    pr_gf["fig_name"] = fig_dir+"05-MEDIA_PESO_ESCMAE.png"

    __grafico(**pr_gf)
  except:
    print("Gráfico de peso por escolaridade da mãe não foi obtido")
    return None

  try:
    # Plotando o sexto gráfico
    pr_gf["values"] = "APGAR1"
    pr_gf["index"] = "GESTACAO"
    pr_gf["aggfunc"] = "mean"
    pr_gf["title"] = f"Média do APGAR1 por semanas de gestação{dados}"
    pr_gf["xlabel"] = "Semanas de Gestação"
    pr_gf["ylabel"] = "APGAR1"
    pr_gf["fig_name"] = fig_dir+"06-APGAR1.png"

    __grafico(**pr_gf)
  except:
    print("Gráfico de APGAR1 por gestação não foi obtido")
    return None

  try:
    # Plotando o sétimo gráfico
    pr_gf["values"] = "APGAR5"
    pr_gf["title"] = f"Média do APGAR5 por semanas de gestação{dados}"
    pr_gf["ylabel"] = "APGAR5"
    pr_gf["fig_name"] = fig_dir+"07-APGAR5.png"

    __grafico(**pr_gf)
  except:
    print("Gráfico de APGAR5 por gestação não foi obtido")
    return None