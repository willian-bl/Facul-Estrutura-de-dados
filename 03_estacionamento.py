"""
Exercício PILHAS - Estacionamento

Um estacionamento possui uma única alameda para guardar os carros que serão
estacionados. Existe apenas uma entrada/saída no estacionamento, em uma
extremidade da alameda. Se chegar um cliente para retirar um carro que não seja o
mais próximo da saída, todos os carros bloqueando seu caminho sairão do
estacionamento, o carro do cliente será manobrado para fora do estacionamento, e
os outros carros voltarão a ocupar a mesma sequência inicial. Escreva um programa
em python que processe um conjunto de entradas. Cada entrada contém um 'E', de
entrada, ou um 'S', de saída, e o número da placa do carro. Presume-se que os
carros cheguem e partam na ordem que chegaram no estacionamento. O
programa deve imprimir uma mensagem sempre que um carro sair do
estacionamento. Quando um carro sair do estacionamento, a mensagem deverá
incluir o número de vezes em que o carro foi manobrado para fora do
estacionamento para permitir que outros carros saíssem.

"""


from os import system
from funcoes_pilhas import *
from time import sleep

class Veiculo:  # No estacionamento (representado por uma pilha), serão armazenados objetos do tipo Veiculo
    def __init__(self, placa):
        self.placa = placa
        self.manobras = 0


def entradaEstacionamento(estacionamento, placa_veiculo):
    if estaEstacionado(estacionamento, placa_veiculo):
        print('Já existe um veículo no estacionamento com essa placa!')
        return

    v = Veiculo(placa=placa_veiculo)
    push(estacionamento, v)
    print(f'Veículo com a placa {placa_veiculo} adicionado no estacionamento!')

    
def estaEstacionado(estacionamento, placa_veiculo):
    """Verifica se um veículo com determinada placa está no estacionamento"""
    aux = []
    estacionado = False

    while not vazia(estacionamento):
        v = pop(estacionamento)
        push(aux, v)

        if v.placa == placa_veiculo:
           estacionado = True
           break

    while not vazia(aux):
        push(estacionamento, pop(aux))

    return estacionado 
        

def saidaEstacionamento(estacionamento, placa_veiculo):
    if vazia(estacionamento):
        print('Estacionamento vazio!')
        return
    
    if not estaEstacionado(estacionamento, placa_veiculo):
        print('O veículo com a placa informada não está no estacionamento!')
        return
    
    aux = []
    while not vazia(estacionamento):
        v = pop(estacionamento)
        if v.placa == placa_veiculo:
            print(f'Veículo retirado do estacionamento com sucesso! \nPlaca: {v.placa} | Nº de Manobras: {v.manobras}')
            break
        push(aux, v)
    
    while not vazia(aux):
        v = pop(aux)
        v.manobras += 1
        push(estacionamento, v)


def printaEstacionamento(estacionamento):
    print('\nEstacionamento agora:')
    if vazia(estacionamento):
        print('O estacionamento está vazio! \n')
        return

    aux = []
    print()
    while not vazia(estacionamento):
        v = pop(estacionamento)
        print('|', v.placa, '|')
        push(aux, v)
    print('=' * (len(v.placa) + 4), '\n')

    while not vazia(aux):
        push(estacionamento, pop(aux))


estacionamento = []

while True:
    system('cls')
    
    print("===================================== Estacionamento da parada =====================================")
    print('Bem vindo ao estacionamento! \nPara adicionar um veículo, digite "E" seguido do número da placa. Ex: "E ABC1234" \nPara retirar um veículo, digite "S" seguido do número da placa. Ex: "S ABC1234" \nEnvie uma entrada vazia para sair do programa')
    
    printaEstacionamento(estacionamento)

    x = input('> ').strip()
    
    if x.lower().startswith('e'):
        entradaEstacionamento(estacionamento, placa_veiculo=x[2:])

    elif x.lower().startswith('s'):
        saidaEstacionamento(estacionamento, placa_veiculo=x[2:])
    
    elif x == '':
        print('Espero que esteja satisfeito com nossos serviços, até a próxima!')
        sleep(3)
        break

    else:
        print('\nDigite algo válido! Caso queira sair, apenas pressione Enter, sem digitar nada')

    sleep(3)
