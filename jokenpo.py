#Random, while loop, tomada de decisão, funções

import random
    
def play():
    user = input("Qual é sua escolha? \n'pd' para Pedra, 'pp' para Papel, 't' para Tesoura\n")
    while user not in('pd', 'pp', 't'):
        print('\nNão é uma opção válida')
        user = input("Qual é sua escolha? \n'pd' para Pedra, 'pp' para Papel, 't' para Tesoura\n")
        
    computer = random.choice(['pd','pp','t'])
      
    if user == computer:
        return '\nÉ um empate\nSua escolha: '+convert(user)+'\nEscolha do computador: '+convert(computer)
        
    if is_win(user, computer):
        return '\nVocê ganhou\nSua escolha: '+convert(user)+'\nEscolha do computador: '+convert(computer)
    return '\nVocê perdeu\nSua escolha: '+convert(user)+'\nEscolha do computador: '+convert(computer)

def is_win(player, opponent):
    #retorna true se o usuário ganhar
    if(player == 'pd' and opponent == 't') or (player == 't' and opponent == 'pp') or (player == 'pp' and opponent == 'pd'):
        return True
        
def convert(computer):
    if computer == 'pd':
        return 'Pedra'
        
    elif computer == 'pp':
        return 'Papel'
        
    elif computer == 't':
        return 'Tesoura'
        
print (play())
