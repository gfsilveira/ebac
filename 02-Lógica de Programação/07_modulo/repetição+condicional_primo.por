programa {
  funcao inicio() {
    inteiro candidato, i, resto, cont = 0

    escreva("Digite o n�mero para verificar se � primo: \n")
    leia(candidato)

    para(i = 1; i <= candidato; i++){
      resto = candidato % i
      se(resto == 0){
        cont++
      }
    }

    se(cont == 2){
      escreva(candidato, " � primo, pois � dividido por 1 e por ele mesmo \n")
    }senao{
      escreva(candidato, " n�o � primo, pois existem ", cont, " n�meros inteiros que o dividem!! \n")
    }
  }
}
