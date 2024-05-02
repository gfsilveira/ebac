programa {
	funcao inicio() {
		inteiro numeroTeste1, numeroTeste2, resto
		
		escreva("Vamos verificar se os valores digitados são múltiplos.\n ")
		escreva("Digite o primeiro valor: ")
		leia(numeroTeste1)
		escreva("\nDigite o segundo valor: ")
		leia(numeroTeste2)
		
		se(numeroTeste1 > numeroTeste2){
		    resto = numeroTeste1 % numeroTeste2
		    se(resto == 0){
		      escreva("O valor ", numeroTeste1, " é múltiplo de ", numeroTeste2,"!")
		    }
		    senao{
		        escreva("O valor", numeroTeste1, " não é múltiplo de ", numeroTeste2,"!")
		    }
		}
		
		se(numeroTeste2 > numeroTeste1){
		    resto = numeroTeste2 % numeroTeste1
		    se(resto == 0){
		      escreva("O valor ", numeroTeste2, " é múltiplo de ", numeroTeste1,"!")
		    }
		    senao{
		        escreva("O valor", numeroTeste2, " não é múltiplo de ", numeroTeste1,"!")
		    }
		}
		
	}
}
