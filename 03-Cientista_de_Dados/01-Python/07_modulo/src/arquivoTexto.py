class ArquivoTexto:
    def __init__(self, arquivo: str) -> None:
        '''
            Inicializador da classe.
            :param arquivo (str): Caminho do arquivo
            :param conteudo (list): Lista com as linhas do arquivo
        '''
        self.arquivo = arquivo
        self.conteudo = self.__extrair_conteudo()

    def __extrair_conteudo(self) -> list|str:
        '''
          Função que abre o arquivo passado como atributo na instânciação
          da classe.

          :return linhas_listadas (list): Retorna o conteudo ou o erro.
        '''
        try:
          with open(file=self.arquivo, mode="r", encoding="utf8") as file:
              arquivo = file.readlines()

          # Formatando os valores da lista, para obter uma lista de listas
          edita_linhas = lambda x: x.strip().split(sep=",")
          linhas_listadas = list(map(edita_linhas, arquivo))
          return linhas_listadas
        except Exception as error:
          return error

    def extrair_linha(self, numero_linha: int) -> list|str:
        '''
            Função que recupera uma linha da lista instânciada na classe. Caso
            indíce não exista, retorna o erro.

            :param numero_linha (int): Index da linha na lista instanciada.
            :return self.conteudo (list): Retorna o conteudo da lista ou o erro.
        '''
        try:
            return self.conteudo[numero_linha]
        except IndexError as index_error:
            return index_error
        except Exception as exception_error:
            return exception_error