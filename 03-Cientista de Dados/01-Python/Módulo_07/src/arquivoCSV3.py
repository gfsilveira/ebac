from src.arquivoTexto import ArquivoTexto

class ArquivoCSV3(ArquivoTexto):
  def __init__(self, arquivo: str) -> None:
    '''
        Inicializador da classe que extende ArquivoTexto.

        :param arquivo (str): Caminho do arquivo
    '''
    super().__init__(arquivo=arquivo)

  def extrair_coluna_da_linha(self, numero_linha: int, indice_coluna: int) -> str:
    '''
      Método que extrai um valor único de uma coordenada indice/coluna

      :return valor (str): Valor buscado na coordenada indice/coluna ou erro.
    '''
    try:
      coluna = self.extrair_linha(numero_linha=numero_linha)
      valor = coluna[indice_coluna]
      return valor
    except IndexError as error1:
      return error1
    except TypeError as error2:
      return error2