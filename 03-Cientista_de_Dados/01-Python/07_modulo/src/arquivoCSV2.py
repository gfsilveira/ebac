from src.arquivoCSV import ArquivoCSV

class ArquivoCSV2(ArquivoCSV):
  def __init__(self, arquivo: str) -> None:
    '''
        Inicializador da classe que extende ArquivoTexto.

        :param arquivo (str): Caminho do arquivo
    '''
    super().__init__(arquivo=arquivo)

  def extrair_coluna_da_linha(self, numero_linha: int, indice_coluna: str) -> str:
    '''
      Método que extrai um valor único de uma coordenada indice/coluna

      :return valor (str): Valor buscado na coordenada indice/coluna ou erro.
    '''
    try:
      coluna = self.extrair_coluna(nome_coluna=indice_coluna)
      valor = str(coluna[numero_linha])
      return valor
    except IndexError as error:
      return error