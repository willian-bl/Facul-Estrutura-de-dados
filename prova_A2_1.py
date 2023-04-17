"""
Leandro Henrique Guilhermiti de Oliveira
Willian Brito de Lima
"""

# A2 - Primeira prova - Em dupla com consulta
# Conteúdo:
#     *Pilhas
#     *Filas

# ------------------ Funções PILHA --------------------------

# Funções primitivas de pilhas
def push(p, v):
    """Coloca um valor no topo da pilha"""
    p.append(v)


def pop(p):
    """Retira um valor do topo da pilha"""
    return p.pop()


def vazia(p):
    """Verifica se a pilha está vazia ou não. Caso esteja, retorna `True`"""
    return False if p else True


# Função para mostrar pilha
def mostraPilha(p):
    if vazia(p):
        print('Pilha vazia!')
        return

    aux = [] 
    print('Topo:')
    while not vazia(p): 
        v = pop(p)
        print(v) 
        push(aux, v) 

    while not vazia(aux):  
        v = pop(aux)       
        push(p, v)


# ------------------ Funções FILA ---------------------------

# Funções primitivas de filas
def inserir(f, v):
    """Tem como função inserir um elemento no final da fila"""
    f.append(v) 
    

def retirar(f):
    """Tem como objetivo retirar e retornar o elemento do início da fila"""
    return f.pop(0)  


def vazia_fila(f):
    """Retorna `True` se a fila estiver vazia, caso contrário retorna `Falso`"""
    return False if f else True


# Função para mostrar fila
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


# ------------------ EXERCÍCIOS ---------------------------

"""
Exercício 1

Utilizando as funções para manipulação de pilhas, escrever uma função em python que
recebe como parâmetros as pilhas p1, p2 e p3. A função deve inserir o primeiro
elemento de p1 em p3 e em seguida inserir o primeiro elemento de p2 em p3. Depois
inserir o último elemento de p1 em p3 e em seguida inserir o último elemento de p2
em p3.

"""

def retorna_primeiro_e_ultimo(p):
    aux = []  # pilha auxiliar

    while not vazia(p):
        v = pop(p)
        push(aux, v)
    
    primeiro = v

    while not vazia(aux):
        x = pop(aux)
        push(p, x)
    
    ultimo = x

    return primeiro, ultimo


def intercala(p1, p2, p3):
    if vazia(p1) or vazia(p2):
        print('Uma das pilhas está vazia!')
        return
    
    primeiro1, ult1 = retorna_primeiro_e_ultimo(p1)
    primeiro2, ult2 = retorna_primeiro_e_ultimo(p2)
    push(p3, primeiro1)
    push(p3, primeiro2)
    push(p3, ult1)
    push(p3, ult2)


print('Exercício 1 \n')

p1 = []
push(p1, 1)
push(p1, 2)
push(p1, 3)
push(p1, 4)
push(p1, 5)
# mostraPilha(p1)

p2 = []
push(p2, 11)
push(p2, 12)
push(p2, 13)
push(p2, 14)
push(p2, 15)
# mostraPilha(p2)

p3 = []

intercala(p1, p2, p3)
print('p1:')
mostraPilha(p1)
print('\np2:')
mostraPilha(p2)
print('\np3:')
mostraPilha(p3)


"""
Exercício 2
Utilizando as funções para manipulação de filas, escrever uma função em python para
mostrar o maior elemento par de uma fila de números inteiros
"""

def maiorPar(f):
    aux = [] # Fila auxiliar
    primeira_iter = True
    maior = None

    while not vazia_fila(f):
        v = retirar(f)
        inserir(aux, v)
        if v % 2 == 0:
            if primeira_iter:
                maior = v
                primeira_iter = False
            elif v > maior:
                maior = v
        
    while not vazia_fila(aux):
        inserir(f, retirar(aux))
    
    if maior == None:
        print("A fila está vazia ou não há elementos pares!")
    else:
        print(f"Maior par {maior}")


print('\n\nExercício 2 \n')

f = []

inserir(f, 15)
inserir(f, 1)
inserir(f, 48)
inserir(f, 12)
inserir(f, 98)
inserir(f, 57)
inserir(f, 101)
inserir(f, 17)

maiorPar(f)
mostraFila(f)


"""
Exercício 3

Utilizando as primitivas para manipulação de pilhas, escrever uma função em python
para calcular o valor da média aritmética dos elementos armazenados em uma pilha
de números inteiros e depois, retirar da pilha todos os elementos maiores que o valor
da média anteriormente calculado.
"""

def retirarMaiorMedia(p):
    aux = [] # Pilha auxiliar
    soma = 0
    qtd = 0

    while not vazia(p):
        v = pop(p)
        push(aux, v)
        soma += v
        qtd += 1

    if qtd != 0:
        media = soma / qtd

    while not vazia(aux):
        x = pop(aux)
        if x <= media:
            push(p, x)

print('\n\nExercício 3 \n')

p0 = [] # Pilha vazia
print('P0:')  
mostraPilha(p0)
retirarMaiorMedia(p0)
mostraPilha(p0)

print('\nP2:')       
mostraPilha(p2)
retirarMaiorMedia(p2)
mostraPilha(p2)

print('\nP3:')       
mostraPilha(p3)
retirarMaiorMedia(p3)
mostraPilha(p3)
