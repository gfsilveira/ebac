import sys
import os

from src.gera_grafico import gera_graficos


def inicializa() -> None:
    '''
        Função de inicialização do app.
    '''
    # Verifica o caminho da pasta atual do sistema
    path = sys.argv[0].replace("main.py","")

    # Muda a pasta de trabalho
    os.chdir(path)

    if len(sys.argv) == 1:
    # Se não for passado nenhum argumento, gera os gráficos para o mês anterior
        gera_graficos()
    else:
        try:
            # Meses do ano.
            meses = [
                "JAN",
                "FEV",
                "MAR",
                "ABR",
                "MAI",
                "JUN",
                "JUL",
                "AGO",
                "SET",
                "OUT",
                "NOV",
                "DEZ"
            ]
            verifica_entrada = True
            # Para todos os argumentos passados
            for argv in sys.argv:
                # Caso sejam abreviaturas dos meses do ano 
                if argv in meses:

                    # Será obtido o index do mês
                    mes = meses.index(argv)

                    # E passado como parâmetro da função, para obter os gráficos
                    gera_graficos(mes=mes)

                    # Verifica se os dados foram salvos
                    verifica_entrada = False
            
            if verifica_entrada:
                print("Algum dos parâmetros passados não está correto!")
                return None
        except:
            print("Algumas das informações enviadas não foram reconhecidas.")
            return None
    return None

if __name__ == "__main__":
    # Rodando a função de inicialização do app
    inicializa()