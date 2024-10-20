from src.test import Test

def inicia(nome: str) -> None:
    novo = Test(nome)
    print(novo.name)


if __name__ == "__main__":
    inicia("Testando")
