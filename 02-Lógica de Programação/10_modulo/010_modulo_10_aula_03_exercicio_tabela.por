programa {
	funcao inicio(){
		cadeia nome[3] = {"Joelmo", "Maria", "Gaspar"} 
		real horasTrabalhadas[] = {23.5, 55.0, 44.0}
		inteiro numeroFilhos[] = {5, 2, 4}
		caracter fumante[] = {'N', 'S', 'S'}
		
		escreva("\n||Nome \t\t||Horas Trabalhadas \t\t||Numero de filhos \t\t||Fumante\n")
		
		para(inteiro i = 0; i < 3; i++){
		    escreva("\n",nome[i],"\t\t\t\t\t",horasTrabalhadas[i],"\t\t\t\t",numeroFilhos[i],"\t\t\t\t\t",fumante[i])
		}
		
		escreva("\n\n")
	}
}