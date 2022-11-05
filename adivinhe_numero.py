#bibliotecas, tomada de decisão, loop, funções
import random

def guess(num):
    numero_aleatorio = random.randint(1,num)
    escolha = 0
    while escolha != numero_aleatorio:
        escolha = int(input(f'Adivinhe um número entre 1 e {num}: '))
        if escolha < numero_aleatorio:
            print('O número que você digitou é menor do que o escolhido. Tente novamente\n')
        elif escolha > numero_aleatorio:
            print('O número que você escolheu é maior do que o escolhido. Tente novamente\n')
    
    print(f'Parabéns, você acertou! O número era {numero_aleatorio}')

guess(10)
