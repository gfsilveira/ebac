programa {
	funcao inicio() {
		caracter tabuleiro[3][3]
		
		para(inteiro i = 0; i < 3; i++){
		    para(inteiro j = 0; j < 3; j++){
		        tabuleiro[i][j] = ' '
		    }
		}
		
		para(inteiro i = 0; i < 3; i++){
		    para(inteiro j = 0; j < 3; j++){
		        escreva("[",tabuleiro[i][j],"]")
		    }
		    escreva("\n")
		}
		escreva("\n\n")
		
		tabuleiro[0][2] = 'X'
		tabuleiro[1][1] = 'X'
		tabuleiro[2][0] = 'X'
		
		para(inteiro i = 0; i < 3; i++){
		    para(inteiro j = 0; j < 3; j++){
		        escreva("[",tabuleiro[i][j],"]")
		    }
		    escreva("\n")
		}
		
		/*Aqui começa o teste para verificar quem vence.*/
		
		/*Teste para as linhas.*/
		para(inteiro i = 0; i < 3; i++){
		    se((tabuleiro[i][0] == 'X')e(tabuleiro[i][1] == 'X')e(tabuleiro[i][2] == 'X')){
		        escreva("Pessoa que escolheu (X) venceu!")
		    }
		    senao se((tabuleiro[i][0] == 'O')e(tabuleiro[i][1] == 'O')e(tabuleiro[i][2] == 'O')){
		        escreva("Pessoa que escolheu (O) venceu!")
		    }
		}
		
		/*Teste para as colunas.*/
		para(inteiro i = 0; i < 3; i++){
		    se((tabuleiro[0][i] == 'X')e(tabuleiro[1][i] == 'X')e(tabuleiro[2][i] == 'X')){
		        escreva("Pessoa que escolheu (X) venceu!")
		    }
		    senao se((tabuleiro[0][i] == 'O')e(tabuleiro[1][i] == 'O')e(tabuleiro[2][i] == 'O')){
		        escreva("Pessoa que escolheu (O) venceu!")
		    }
		}
		
		/*Teste para a primeira diagonal.*/
	    se((tabuleiro[0][0] == 'X')e(tabuleiro[1][1] == 'X')e(tabuleiro[2][2] == 'X')){
	        escreva("Pessoa que escolheu (X) venceu!")
		    }
        senao se((tabuleiro[0][0] == 'O')e(tabuleiro[1][1] == 'O')e(tabuleiro[2][2] == 'O')){
		    escreva("Pessoa que escolheu (O) venceu!")
        }
        
        /*Teste para a segunda diagonal.*/
	    se((tabuleiro[0][2] == 'X')e(tabuleiro[1][1] == 'X')e(tabuleiro[2][0] == 'X')){
	        escreva("Pessoa que escolheu (X) venceu!")
		    }
        senao se((tabuleiro[0][2] == 'O')e(tabuleiro[1][1] == 'O')e(tabuleiro[2][0] == 'O')){
		    escreva("Pessoa que escolheu (O) venceu!")
        }
        senao{
            escreva("Deu velha! Jogue novamente!")
        }
	}
}
