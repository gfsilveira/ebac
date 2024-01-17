programa {
    inclua biblioteca Texto --> txt
	funcao inicio() {
		cadeia palavra1
		inteiro tamanhoPalavra
		caracter letra1
		
		escreva("Digite uma palavra: \n")
		leia(palavra1)
		
		tamanhoPalavra = txt.numero_caracteres(palavra1)
		
		para(inteiro x = 0; x < tamanhoPalavra; x++){
		    letra1 = txt.obter_caracter(palavra1, x)
		    escreva(letra1,"\n")
		}
		
		escreva(tamanhoPalavra)
	}
}
