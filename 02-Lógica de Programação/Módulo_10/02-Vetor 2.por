programa {
  funcao inicio() {
    inteiro tamanho

    escreva("Qual o tamanho do vetor? ")
    leia(tamanho)

    cadeia vetor[tamanho]

    para(inteiro i = 0; i < tamanho; i++){
      escreva("Entrada ", i+1, ": ")
      leia(vetor[i])
      escreva(vetor, "\n")
    }
  }
}
