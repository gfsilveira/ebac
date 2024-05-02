programa {
  inclua biblioteca Util --> utl
  funcao inicio() {
    inteiro dados[3]
    inteiro notas[] = {2, 3, 45, 10, 20, 30, 30}, tamanho

    escreva("Insira um número: ")
    leia(dados[0])

    escreva(dados[0])

    escreva("\n-------------------\n")

    escreva(notas[2])

    escreva("\n-------------------\n")

    tamanho = utl.numero_elementos(notas)
    escreva(tamanho)

    escreva("\n-------------------\n")

    para(inteiro i = 0; i < tamanho; i++){
      escreva(notas[i], "\n")
    }
  }
}
