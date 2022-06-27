import os
from random import randint
import time
import psutil

def contido(n, lista):
    if (n in lista):
        return True
    else:
        return False


def novo(n1, n2):
    numeros = []

    while (len(numeros) < 10):
        num = randint(n1, n2)
        if (contido(num, numeros) == False):
            numeros.append(num)
    return numeros


def numero_sorteado(n1, n2, nsort):
    while True:
        n = randint(n1, n2)
        if not contido(n, nsort):
            nsort.append(n)
            return n


def limpar():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')



num = (50000)
cartelas = []
sorteado = []
ganhadores = []
vencedor = False
count = 0

qtde = 0
for i in range(num):
    lista = novo(1, 50)
    cartelas.append(lista)

while not vencedor:
    sort = numero_sorteado(1, 50, sorteado)
    print("soBET")
    print(f"Número sorteado: {sort}")
    for i in range(len(cartelas)):
        qtde = 0
        for j in range(len(cartelas[i])):
            if (contido(cartelas[i][j], sorteado) == True):
                qtde += 1
        print(f"Jogador {i + 1}", (cartelas[i]), qtde)
        if qtde == 10:
            vencedor = True
            ganhadores.append(i)
    if not vencedor:
        print("Ainda não temos vencedores.")
        count = count + 1
        print('A quantidade de números sorteados até o momento é: ',count)
        #time.sleep(1)
        #limpar()

print()
for s in ganhadores:
    print(f"Jogador {s + 1} completou a cartela! ", cartelas[s])

print("Números sorteados: ", sorteado)
