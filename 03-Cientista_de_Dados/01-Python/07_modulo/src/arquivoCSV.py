from src.arquivoTexto import ArquivoTexto

class ArquivoCSV(ArquivoTexto):
    def __init__(self, arquivo: str) -> None:
        '''
            Inicializador da classe que extende ArquivoTexto.

            :param arquivo (str): Caminho do arquivo
            :param conteudo (list): Lista com as linhas do arquivo
            :param colunas (list): Os elementos são os nome das colunas
        '''
        super().__init__(arquivo=arquivo)

        self.colunas = self.__extrair_nome_colunas()

    def __extrair_nome_colunas(self) -> list:
        '''
          Método que retorna o nome das colunas do arquivo.

          :return nome_colunas (list): Nome das colunas do arquivo.
        '''
        nome_colunas = self.extrair_linha(numero_linha=0)
        return nome_colunas


    def __converte_lista_para_dicionario(self) -> list:
        '''
            Método map para unir cada uma das varíáveis com seu index em um
            dicionário, usando a função zip.

            :return conteudos (list): Lista com o conteudo em formato dict
        '''
        obtendo_conteudo = lambda x: dict(zip(self.conteudo[0], x))
        conteudos = list(map(obtendo_conteudo, self.conteudo[1:]))
        return conteudos


    def extrair_coluna(self, nome_coluna: str) -> list|str:
        '''
            Método que recebe como parâmetro o indice da coluna e retorna o
            valor em questão.

            :param nome_coluna (str): Indice da coluna no dicionario conteudo.
            :return conteudo_coluna (list): Retorna o conteudo da lista ou o erro.
        '''
        try:
          conteudo_dict = self.__converte_lista_para_dicionario()
          conteudo_coluna = [conteudo[nome_coluna] for conteudo in conteudo_dict]
          return conteudo_coluna
        except KeyError as error:
          return f"Coluna {error} não encontrada"