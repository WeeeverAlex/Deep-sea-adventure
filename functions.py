from random import *
from re import A 
import sys
import time

posicao_jogador = []
tesouros_carregados = []

# Funcao: Pega no stackoverflow, para colocar slow entre os prints
def print_slow(str): 
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.02)  

#Função: Definir o valor dos tesouros
def sorteador_tesouros(posicao):
    if posicao <= 8:
        valor_tesouros = randint(0,3)
    elif posicao > 8 and posicao < 17:
        valor_tesouros = randint(4,7)
    elif posicao > 16 and posicao < 25:
        valor_tesouros = randint(8,11)
    else:
        valor_tesouros = randint(12,15)
    return valor_tesouros     

#Função: sorteio dos dados
#dado1
def numero_dado1():
    dado1 = randint(1,3)
    return dado1
#dado2
def numero_dado2():
        dado2 = randint(1,3)
        return dado2

#Função: Definir posição do jogador no print
def posicao_na_lista(lista,jogador,posicao):
    lista_retorno = []
    for elem in lista:
        lista_retorno.append(elem)
    lista_retorno[posicao-1] = jogador
    return lista_retorno

#Calcular a total de pontos do jogador
def total_pontos(lista):
    return sum(lista)        
       

