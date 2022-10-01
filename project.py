from functions import *
import sys
import time
from random import *


def print_slow(str): #Funcao pega no stackoverflow, para colocar slow entre os prints
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.02) 
   
#variaveis
tesouros_carregados = []
posicao = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32]
posicao_jogador = 7
len(tesouros_carregados) < 4
dado1 = numero_dado1()
dado2 = numero_dado2()
valor_tesouros = sorteador_tesouros(posicao)
tesouro1 = 0
tesouro2 = 0
tesouro3 = 0
tesouro4 = 0
soma_dado = dado1 + dado2
posicao_atual = posicao_jogador - soma_dado 

#começo
print()
print_slow('=================================================')
print()
print_slow('         Bem-vindo ao Aventura em alto mar!          ')
print()
print_slow('=================================================')
print()
print_slow('Boa sorte para encontrar tesouros valiosos e tome cuidado para não ficar sem oxigênio =)')
print()
começar = input('pressione C para começar: ').upper()
print()
if começar == 'C':
    print('BEM VINDO AO FUNDO DO MAR!')      
print()

#subamrino
print()
print_slow('             ____')
print()
print_slow('            ()_  |')
print()
print_slow('---------------| |-------------------------------')
print()
print_slow('            ___| |___')
print()
print_slow('      _____/_________\_____    _          O') 
print()
print_slow('     /                     \  / )           o')
print()
print_slow('    (   O       O       O    )  z)        o')
print()
print_slow('     \______________________/ \_)')
print()
print_slow('               [1]  [2]  [3]  [4]  [5] [6]  [7]  [8]'        )
print()
print_slow('                                                [9] ')
print()
print_slow('        [16]  [15]  [14]  [13]  [12]  [11]  [10] ')
print()
print_slow('      [17] ')
print()
print_slow('          [18]  [19]  [20]  [21]  [22]  [23] ')
print()
print_slow('                                      [24] ')
print()
print_slow('      [30]  [29]  [28]  [27]  [26]  [25]')
print()
print_slow('    [31]')
print()   
print_slow('       [32]')
print()

#respirar
print_slow('FASE: RESPIRAR')
respirar = input('pressione R para respirar: ').upper()
print()
while respirar == 'R':
    respirou = len(tesouros_carregados)
    oxigenio = 25
    if respirou < oxigenio:
        oxigenio_atual = oxigenio - respirou
        print_slow(f'o nivel de oxigênio está em {oxigenio}')
        oxigenio -= 1
        print()
        print_slow(f'você consumiu {respirou} de oxigênio nesta rodada!')
        print()
        print_slow(f'o nivel atual de oxigênio está em {oxigenio_atual}')
        print()
        respirou += 1
        break
print()    

#avançar ou retroceder
print('FASE: AVANÇAR OU RETROCEDER')
print()
avançar_retroceder = input('Você deseja AVANÇAR ou RETROCEDER? Digite [A] AVANÇAR ou [R] RETROCEDER: ').upper()
if avançar_retroceder == 'A':
    print('Você desejou avançar')
elif avançar_retroceder == 'R':
    print('Você desejou retroceder para o submarino')
print()

#dados 
rolar_dados = input('Pressione ENTER para rolar os dados ')
print()
print_slow(f'Os dados foram rolados e você tirou DADO 1: {dado1} e DADO 2: {dado2}')
print()
print_slow(f'A soma dos DADO 1 e DADO 2 foi de {soma_dado} e agora você está na profundidade {posicao_atual}')
print()
if soma_dado < len(tesouros_carregados):
        print_slow('Que Pena =(')
        print()
        print_slow(f'Você não conseguiu andar nesta rodada. Voce esta carregando {len(tesouros_carregados)} tesouros e tirou {soma_dado} na soma de dados')
elif posicao_jogador == 0:
    print()
    print_slow('Parabéns! Você está no submarino!')
    print()
    print_slow(f'Sua pontuação final é de {valor_tesouros}')
else:
    while True:
        print()
        soltar_vasculhar = input('Você deseja soltar algum tesouro ou vasculhar o fundo do mar? Pressione S para soltar ou V para vasculhar: ').upper() 
        if soltar_vasculhar == 'V':
            vasculhar = input('Pressione ENTER para vaculhar: ')
            print()
            print(f'Você vasculhou o fundo do mar e encontrou um tesouro que vale {valor_tesouros}')
            print()
            ficar_tesouro = input('Pressione T se você deseja ficar com o tesouro: ').upper()
            print()
            break
        elif soltar_vasculhar == 'S':
            soltar = input('Pressione ENTER para soltar: ')
            print()
            print(f'Seus tesouros são: [1] {tesouro1} - [2] {tesouro2} - [3] {tesouro3} - [4] {tesouro4} ')
            print()
            tesouro_solto = input('Indique qual tesouro desses você deseja soltar [1], [2], [3] ou [4]: ')
                
            print()        
            print(f'Seus tesouros são: [1] {tesouro1} - [2] {tesouro2} - [3] {tesouro3} - [4] {tesouro4} ')  

            print('Entrada invalida').upper()    
              




