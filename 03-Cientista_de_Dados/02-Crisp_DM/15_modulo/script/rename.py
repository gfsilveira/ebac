import os
import sys

def rename_files(link: str = ".") -> None:

    os.chdir(link)

    lista_files = os.listdir()

    lista_files = [i for i in lista_files if "módulo" in i]

    for file_index in range(len(lista_files)):
        old = lista_files[file_index]
        new = old.replace("ó","o")
        os.rename(old, new)

    lista_files_new = os.listdir()
    print(lista_files_new)

    return None


if __name__ == "__main__":
    rename_files(link=sys.argv[1])
