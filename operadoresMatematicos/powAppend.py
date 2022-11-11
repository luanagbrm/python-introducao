import math
#Exibir todos os dígitos positivos menores que 'n' elevados a 2 em linhas separadas
is_int = False

#tratamento de input fora das instruções
while is_int == False:
        try:
            n = int(input('Digite um número inteiro positivo maior que 0\n'))
            is_int = True
        except:
            print('Por favor, siga as intruções')
order = []
    
while n < 1:
    is_int = False
    try:
        n = int(input('Siga as instruções. Digite um número inteiro positivo maior que 0\n'))
        is_int = True
    except:
        print('Por favor, siga as intruções')

#Execução do exercício proposto
for i in range(n):
    order.append(i)
            
for i in order:
    order[i] = pow(order[i],2)
    print(order[i])