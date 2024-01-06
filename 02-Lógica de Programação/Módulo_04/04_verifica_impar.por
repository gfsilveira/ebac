/*****      Professor Francisco Viana       *****/
/*****      Verifica se o número é ímpar    *****/

programa {
	funcao inicio() {
		inteiro candidatoImpar, resto
		
		escreva("Olá! Sou um progama que verifica se o número digitado é ímpar. Por favor, digite um número: \n")
		leia(candidatoImpar)
		escreva("Você digitou o número ", candidatoImpar," .\n")
		
		/*Aqui está a aplicação do operador: resto da divisão (%).*/  
		resto = candidatoImpar % 2
		
		se(resto != 0){
		    escreva("O número que você digitou é ímpar.\n")
		}
		senao{
		    escreva("O número que você digitou não é ímpar.\n")
		}
		
	}
}
