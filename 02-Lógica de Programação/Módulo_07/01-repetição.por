programa {
  funcao inicio() {
    inteiro tamanhoSequencia, par

    escreva("Digite um valor: \n")
    leia(tamanhoSequencia)

    para(par = 0; par <= tamanhoSequencia; par += 2){
      escreva(par, "\n")
    }
  }
}
