programa {
	funcao inicio() {
		inteiro tamanhoSequencia, contador = 1
		
		escreva("Vamos escrever uma sequência de números inteiros!\nDigite o tamanho da sequência: ")
		leia(tamanhoSequencia)
		escreva("Você digitou ", tamanhoSequencia," como tamanho!\n")
		
		enquanto(contador <= tamanhoSequencia){
		    escreva(contador,"-")
		    contador = contador + 1
		}
	}
}
