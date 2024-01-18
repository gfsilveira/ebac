programa {
  inclua biblioteca Util --> utl
  funcao inicio() {
    inteiro valores_0[][] = {
                            {1,2,3},
                            {4,5,6},
                            {7,8,9}
                          }

    escreva(valores_0)

    escreva("\n==================================\n")

    inteiro valores[3][4]
    inteiro valor_1[] = {1,2,3,4}
    inteiro valor_2[] = {4,5,6,7}
    inteiro valor_3[] = {7,8,9,0}

    valores[0] = valor_1
    valores[1] = valor_2
    valores[2] = valor_3

    escreva(valores)

    escreva("\n==================================\n")

    escreva(utl.numero_elementos(valores[0]))
  }
}
