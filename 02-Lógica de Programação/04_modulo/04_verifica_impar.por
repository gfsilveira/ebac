/*****      Professor Francisco Viana       *****/
/*****      Verifica se o n�mero � �mpar    *****/

programa {
	funcao inicio() {
		inteiro candidatoImpar, resto
		
		escreva("Ol�! Sou um progama que verifica se o n�mero digitado � �mpar. Por favor, digite um n�mero: \n")
		leia(candidatoImpar)
		escreva("Voc� digitou o n�mero ", candidatoImpar," .\n")
		
		/*Aqui est� a aplica��o do operador: resto da divis�o (%).*/  
		resto = candidatoImpar % 2
		
		se(resto != 0){
		    escreva("O n�mero que voc� digitou � �mpar.\n")
		}
		senao{
		    escreva("O n�mero que voc� digitou n�o � �mpar.\n")
		}
		
	}
}
