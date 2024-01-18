#/usr/bin/python3
#importando a biblioca math
import math
#criado a função calc_hipotenusa com calc para saber o valor colocado anteriormente pelo argumento
def calc_hipotenusa(calc):
	#se o valor de calc dado pelo usuario for 1, ele vai utilizar o if = 1 para fazer o primeiro calculo, da hipotenusa
    	if calc == '1':   
            cat1 = float(input('coloque o ca:'))
            cat2 = float(input('coloque o co:'))

            calcs = cat1*cat1
            calc2 = cat2*cat2
	   
            adicao = calcs + calc2
            
            #utilizando if para a verificação do numero feito após os calculos para saber se é um numero primo, caso for, ele vai continuar normalmente a conta
            if verificar(adicao):
                #continuando a conta indo uma função da biblioteca math, utilizando math.sqrt para calcular a raiz do numero não primo
                result = math.sqrt(adicao)
		#imprime o resultado, juntamente com 2 decimais para ter a certeza da precisão do resultado
                print('\nO resultado do hipotenusa: {:.2f}'.format(result))
            else:
            	#fazendo a mesma impressão, só que dessa vez, se o numero for primo ele vai imprir diretamente o calculo feito, resultando na raiz de tal numero
                print(f'\nO resultado é raiz quadrada: {adicao:.2f}')
            #aqui ele retorna como false, para quebrar o laço dado pelo while
            return False
        #se o resultado não for igual a 1 ele vai ver a segunda opção que é o calc == 2 o qual vai calcular o cateto dessa vez
    	elif calc == '2':
           cat1 = float(input('coloque seu cateto:'))
           h = float(input('coloque sua hipotenusa:'))
           
           cat2 = cat1*cat1
           h2 = h*h
           
           calcs = h2 - cat2
	   #agora com a conta feita, iremos verificar a conta, ver se ela irá bater com os numeros primos da função "verificar", se não for numero primo, ele irá continuar a conta, fazendo o calculo da raiz e por fim, printar o calculo
           if verificar(calcs):
                result = math.sqrt(float(calcs))
                
                print('\nO resultado do cateto é: {:.2f}'.format(result))
           #se o calculo de verificar for primo, ele não irá fazer a conta de raiz, passando somente o valor dado no resultado na variavel calcs
           else:
           	print('\nO resultado do cateto é a raiz quadrada: {:.2f}'.format(calcs))
           #retornar false, assim, finalizando o laço com while
           return False
    	#ultima opção, caso o valor dado pelo calc for igual a 0 ele irá sair do programa, printando "Saindo..." e assim, finalizando o laço com return False
    	elif calc == '0':
           print('\nSaindo...')
           return False
        #aqui vamos verificar se o numero dos calculos é primo ou não, utilizando falso e verdadeiro
def verificar(n):
	#abrindo um arquivo retornando em uma variavel "verif"
	verif = open('numeros')
	#aqui iremos fazer "verif" ser lido, colocando enumeração com a virgula para separar os numeros primos, no arquivo
	verif = verif.read().split(',')
	#aqui vamos criar uma variavel com o booloan True
	primo = True
	#aqui iremos criar num verificando numero por numero pelo verif
	for num in verif:
		#aqui, vamos dar tirar o espaço dos numeros primos, assim evitando que todos os numeros se tornem verdadeiros, sendo todos int, verificando se todos os numeros são iguais a n "ou no caso o numero que será comparado"
		if int(num.strip()) == int(n):
			#se o "n" for igual a algum num, ele irá ser igual a false, assim o programa vai se encerrar com numero retornando false
			primo = False
	#se o numero não for primo, ele retornarar como True "verdadeiro" assim, continuando a conta com raiz		
	return primo
#colocando valor verdadeiro em abc
abc = True
#vamos dar um while para fazer um laço, sendo valor abc, ou seja, verdadeiro
while abc:
	#Aqui vamos retornar as perguntas para a variante P, utilizando strip para retirar os espaços da pergunta
	P = input('1-Hipotenusa \n'
		  '2-Cateto \n'
		  '0-Sair \n'
		  '---> ').strip()[0]
        #retornar a função calc para abc para saber se o valor será retornado False, se caso for, o laço é quebrado, saindo do programa
	abc = calc_hipotenusa(P)
