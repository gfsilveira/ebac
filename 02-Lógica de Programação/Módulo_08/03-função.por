programa {
  funcao somador(real a, real b){
    real real_soma = a + b
    retorne real_soma
  }

  funcao escrever(real a, real b){
    real c = somador(a, b)
    escreva("O valor da soma é: ", a, " + ", b, " = ", c, "\n")
  }
  
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
      escrever(valor_1, valor_2)
    }
  }
}
