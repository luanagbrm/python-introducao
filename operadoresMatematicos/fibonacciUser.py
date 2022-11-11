#Sequência de Fibonacci

#Formada pela soma dos dois números anteriores ao termo na sequência. 
#Exemplo: 4° termo = 2, 5° Termo = 3, logo, 6° termo -> 2+3 = 5 
is_int = False
v1, v2 = 0, 1
i = 1

#tratamento de input fora das intruções
while is_int == False:
    try:
        nFinal = int(input('Digite um número inteiro positivo acima de 0\n'))
        is_int = True
    except:
        print('Por favor, siga as intruções')

while nFinal < 1:
    try:
        nFinal = int(input('Siga as instruções. Digite um número inteiro positivo acima de 0\n'))
    except:
        print('Por favor, siga as instruções')


#Execução do exercício proposto
if nFinal == 1:
    print('Sequência de fibonacci até o '+str(nFinal)+'° termo')
    print(v1)

else:
    print('Sequência de fibonacci até o '+str(nFinal)+'° termo')
    for i in range(nFinal):
        print(v1)
        vSequencia = v1 + v2
        v1 = v2
        v2 = vSequencia
        i += 1
