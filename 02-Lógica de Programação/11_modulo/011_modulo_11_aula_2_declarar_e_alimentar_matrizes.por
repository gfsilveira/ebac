programa {
	funcao inicio() {
	inteiro matriz1[3][3], matriz2[3][3]
	
	matriz1[0][0] = 1
	matriz1[0][1] = 2
	matriz1[0][2] = 3
	matriz1[1][0] = 4
	matriz1[1][1] = 5
	matriz1[1][2] = 6
	matriz1[2][0] = 7
	matriz1[2][1] = 8
	matriz1[2][2] = 9
	
	escreva("[",matriz1[0][0],"]","[",matriz1[0][1],"]","[",matriz1[0][2],"]\n")
	escreva("[",matriz1[1][0],"]","[",matriz1[1][1],"]","[",matriz1[1][2],"]\n")
	escreva("[",matriz1[2][0],"]","[",matriz1[2][1],"]","[",matriz1[2][2],"]\n")
	
	escreva("\n\n")
	
	para(inteiro i = 0; i < 3; i++){
	    para(inteiro x = 0; x < 3; x++){
	        escreva("Digite um valor: \n")
	        leia(matriz2[i][x])
	    }
	}
	
	escreva("\n\n")
	
	para(inteiro i = 0; i < 3; i++){
	    para(inteiro x = 0; x < 3; x++){
	        escreva("[",matriz2[i][x],"]")
	    }
	    escreva("\n")
	}

	
	}
}
