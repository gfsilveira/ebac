programa {
	funcao inicio() {
		real matrizNotas[2][3]
		
		para(inteiro j = 0; j < 2; j++){
		    para(inteiro z = 0; z < 2; z++){
		        escreva("Digite a nota: \n")
		        leia(matrizNotas[j][z])
		    }
		    matrizNotas[j][2] = (matrizNotas[j][0] + matrizNotas[j][1]) / 2
		}
		
		para(inteiro j = 0; j < 2; j++){
		    para(inteiro z = 0; z < 3; z++){
		        escreva("|||",matrizNotas[j][z],"\t\t")
		    }
		    escreva("\n")
		}
	}
}
