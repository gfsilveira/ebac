programa {
	funcao inicio() {
		real num1, num2
		
		escreva("Digite o valor \n")
		leia(num1)
		
		escreva("Digite o valor \n")
		leia(num2)
		
		somador(num1, num2)
		
	}
	
	funcao somador(real a, real b){
	    real c = a + b
	    escreva("A soma é ",c,".\n")
	}
}
