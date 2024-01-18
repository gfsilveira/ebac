programa {
	funcao inicio() {
		cadeia vetorNomes[2]
		
		para(inteiro i = 0; i < 2; i++){
		    escreva("Digite o nome: \n")
		    leia(vetorNomes[i])
		}
		
		para(inteiro i = 0; i < 2; i++){
		    escreva("|||",vetorNomes[i],"\n")
		}
	}
}
