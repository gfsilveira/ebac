programa {
	funcao inicio() {
		caracter vetor1[3], valor1, valor2, valor3
		
		escreva("\nDigite um valor: \n")
		leia(valor1)
		
		escreva("\nDigite um valor: \n")
		leia(valor2)
		
		escreva("\nDigite um valor: \n")
		leia(valor3)
		
		vetor1[0] = valor1
		vetor1[1] = valor2
		vetor1[2] = valor3
		
		escreva("\nO primeiro valor é: ", vetor1[0],"\n")
		escreva("\nO segundo valor é: ", vetor1[1],"\n")
		escreva("\nO terceiro valor é: ", vetor1[2],"\n")
		
	}
}
