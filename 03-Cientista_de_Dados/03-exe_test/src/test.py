class Test:
    def __init__(self, name: str) -> None:
        self.__name = name

    @property
    def name(self) -> str:
        return f"Imprimindo Nome: {self.__name}"
