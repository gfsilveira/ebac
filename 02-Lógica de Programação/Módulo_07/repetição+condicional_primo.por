programa {
  funcao inicio() {
    inteiro candidato, i, resto, cont = 0

    escreva("Digite o número para verificar se é primo: \n")
    leia(candidato)

    para(i = 1; i <= candidato; i++){
      resto = candidato % i
      se(resto == 0){
        cont++
      }
    }

    se(cont == 2){
      escreva(candidato, " é primo, pois é dividido por 1 e por ele mesmo \n")
    }senao{
      escreva(candidato, " não é primo, pois existem ", cont, " números inteiros que o dividem!! \n")
    }
  }
}
