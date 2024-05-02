programa {
  funcao inicio() {
    real valor_1, valor_2, soma
    inteiro i, repetir

    escreva("Quantas repetições? ")
    leia(repetir)
    
    escreva("Digite um valor: ")
    leia(valor_1)

    escreva("Digite um valor: ")
    leia(valor_2)

    para(i = 1; i <= repetir; i++){
      escreva(i, " - ")
      somador(valor_1, valor_2)
    }
  }

  funcao somador(real a, real b){
    real real_soma = a + b
    escreva("O valor da soma é: ", a, " + ", b, " = ", real_soma, "\n")
  }
}
