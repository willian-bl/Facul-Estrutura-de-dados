"""
Exercício FILAS - Intercalar uma fila

Utilizando as funções primitivas para manipulação de filas, escrever uma função em
python para intercalar os elementos da primeira metade de uma fila com os
elementos da segunda metade da mesma fila.

Exemplo:
Fila inicial - antes da intercalação dos elementos
> 10, 20, 30, 40, 50, 60, 70, 80 fim

Fila final - após a intercalação dos elementos
> 10, 50, 20, 60, 30, 70, 40, 80 fim

Obs: Para filas ímpares, uma das metades (o aluno escolhe qual será)
poderá ficar com um elemento a mais que a outra metade, que deverá ser colocado ao final
da fila intercalada
"""


# ------------------------------ FUNÇÕES PRIMITIVAS ------------------------------
def inserir(f, v):
    """Tem como função inserir um elemento no final da fila"""
    # f representa a fila (utilizamos uma lista para representar) e v o valor a ser inserido
    f.append(v)  # insere um valor no final da lista
    

def retirar(f):
    """Tem como objetivo retirar e retornar o elemento do início da fila"""
    return f.pop(0)  # retira um valor do INICIO da lista


def vazia_fila(f):
    """Retorna `True` se a fila estiver vazia, caso contrário retorna `Falso`"""
    return False if f else True


# ------------------------------ FUNÇÕES COMPLEMENTARES ------------------------------
def mostraFila(f):
    if vazia_fila(f):
        print('Fila vazia!')
        return
    
    aux = []  # Meu auxiliar, agora, será uma fila
    print('>', end=' ')
    while not vazia_fila(f):
        v = retirar(f)
        print(v, end=' ')
        inserir(aux, v)
    print('fim')

    while not vazia_fila(aux):
        inserir(f, retirar(aux))


def quantidadeFila(f):
    """Retorna a quantidade de elementos de uma fila"""

    aux = []
    cont = 0
    while not vazia_fila(f):
        v = retirar(f)
        cont += 1
        inserir(aux, v)
    
    while not vazia_fila(aux):
        inserir(f, retirar(aux))
    
    return cont


# ------------------------------ FUNÇÃO PRINCIPAL ------------------------------
def intercala_fila(f):
    metade1 = []  # Fila auxiliar da primeira metade
    metade2 = []  # Fila auxiliar da segunda metade

    tam_fila = quantidadeFila(f)
    
    if tam_fila % 2 == 0:
        metade = tam_fila / 2
    else:
        metade = tam_fila // 2 + 1  # Caso a fila tenha um número ímpar de elementos, a metade1 será maior (terá um elemento a mais)
                                    
    cont = 1
    while not vazia_fila(f):
        v = retirar(f)
        if cont <= metade:   
            inserir(metade1, v)
        else:
            inserir(metade2, v)
        cont += 1
    
    for i in range(tam_fila):  
        if i % 2 == 0 or vazia_fila(metade2):   # Se for par, adiciona valor da metade1; Também adiciona se os valores de metade2 tiverem acabado. Se isso acontecer, quer dizer que
            inserir(f, retirar(metade1))        # A fila tem tamanho ímpar, está na última iteração e falta um elemento de metade1 para ser intercalado.
        elif not vazia_fila(metade2):           # Caso a fila seja de tamanho par, o último elemento estará em metade2, ele vai entrar no elif na última iteração e o código vai sair do for.
            inserir(f, retirar(metade2))


print('Fila de tamanho par:')
fila = []
for i in range(1, 9):
    inserir(fila, i*10)
mostraFila(fila)

print('Intercalando fila...')
intercala_fila(fila)
mostraFila(fila)

print('\nFila de tamanho ímpar:')
fila = []
for i in range(1, 10):
    inserir(fila, i*10)
mostraFila(fila)

print('Intercalando fila...')
intercala_fila(fila)
mostraFila(fila)
