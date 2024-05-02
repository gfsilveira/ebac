programa {
  funcao inicio() {
    inteiro i
    caracter letra_1
    cadeia palavra, vetor_1[2], vetor_2[] = {"Tenta","Mais","um"}

    letra_1 = '°'
    escreva(letra_1, "\n")

    palavra = "entrada"
    escreva(palavra, "\n")

    palavra = "°"
    escreva(palavra, "\n")

    escreva("\n##############################\n\n")

    vetor_1[0] = "Questão"
    vetor_1[1] = "Fundamental"

    para(i = 0; i <= 1; i++){
      escreva(vetor_1[i], "\n")
    }
    
    escreva("\n##############################\n\n")

    para(i = 0; i <= 2; i++){
      escreva(vetor_2[i], "\n")
    }
  }
}
