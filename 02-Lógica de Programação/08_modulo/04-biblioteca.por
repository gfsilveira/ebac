programa {
  inclua biblioteca Matematica --> mat

  funcao inicio() {
    real base, ordem, raiz

    escreva("Valor um: ")
    leia(base)

    escreva("Ordem: ")
    leia(ordem)

    raiz = mat.raiz(base, ordem)
    escreva("A raiz de ", base, " na ordem ", ordem, " é: ", raiz)
  }
}
