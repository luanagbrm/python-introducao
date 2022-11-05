# random, tomada de decisão, loop
import random

def guess(x):
    numero_aleatorio = random.randint(1,x)
    escolha = 0
    while escolha != numero_aleatorio:
        escolha = int(input(f'Adivinhe um número entre 1 e {x}: '))
        if escolha < numero_aleatorio:
            print('O número que você digitou é menor do que o escolhido. Tente novamente\n')
        elif escolha > numero_aleatorio:
            print('O número que você escolheu é maior do que o escolhido. Tente novamente\n')
    
    print(f'Parabéns, você acertou! O número era {numero_aleatorio}')

guess(10)
