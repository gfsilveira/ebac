programa {
	funcao inicio() {
		cadeia nome1, ultimoSobrenome1, nomeCompleto1, nome2, ultimoSobrenome2, nomeCompleto2
		
		escreva("Olá! Vamos verificar o seu registro! Por favor digite seu primeiro nome: \n")
		escreva("Digite seu primeiro nome em letras minúsculas.\n")
		leia(nome1)
		escreva("Digite seu último sobrenome em letras minúsculas.\n")
		leia(ultimoSobrenome1)
		nomeCompleto1 = nome1 + ultimoSobrenome1
		
		escreva("Por favor, vamos repetir a operação.\n")
		
		escreva("Digite seu primeiro nome em letras minúsculas.\n")
		leia(nome2)
		escreva("Digite seu último sobrenome em letras minúsculas.\n")
		leia(ultimoSobrenome2)
		nomeCompleto2 = nome2 + ultimoSobrenome2
		
		se(nomeCompleto1 == nomeCompleto2){
		    escreva("Você digitou corretamente. Muito obrigado!")
		}
		senao{
		    enquanto(nomeCompleto1 != nomeCompleto2){
		        escreva("Você digitou nomes diferentes, por favor, vamos repetir a operação.\n")
		
		        escreva("Digite seu primeiro nome em letras minúsculas.\n")
		        leia(nome2)
	        	escreva("Digite seu último sobrenome em letras minúsculas.\n")
	    	    leia(ultimoSobrenome2)
		        nomeCompleto2 = nome2 + ultimoSobrenome2
		    }
	    escreva("Você digitou corretamente. Muito obrigado!")
		}
	}
}