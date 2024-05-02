programa {
    
	funcao inicio() {
		real hip, cat1, cat2, teste
		
		escreva("Vamos verificar se o triângulo apresentado é triângulo retângulo.\n")
		escreva("Digite o valor do maior lado: \n")
		leia(hip)
		escreva("Digite o valor do segundo lado: \n")
		leia(cat1)
		escreva("Digite o valor do terceiro lado: \n")
		leia(cat2)
		
		se((hip > cat1)e(hip > cat2)){
		    escreva("Você digitou valores adequados!\n")
		    teste = somaQuadrado(cat1,cat2)
		    se((hip*hip) == teste){
		        escreva("O triângulo apresentado é um triângulo retângulo!\n")
		    }
		    senao{
		       escreva("O triângulo apresentado não é um triângulo retângulo!\n") 
		    }
		}
		senao{
		    escreva("Você digitou valores em ordem inadequada! Por favor, comece novamente!")
		}
	}
	
	
	/*Aqui está um exemplo de criação de função para o cálculo de uma parte do problema! Pensamento Computacional: dividir em pequenas soluções!*/
	funcao real somaQuadrado(real b, real c){
        real quadrado
        quadrado = (b*b) + (c*c)
        retorne quadrado
    }
}
