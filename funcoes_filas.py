"""Arquivo com funções usadas para manipulação de filas. Conforme novas funções forem sendo criadas durante as aulas, elas serão adicionadas aqui para serem importadas em outros projetos"""
import funcoes_pilhas

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


def estaNaFila(f, x):
    """Testa se um valor `x` está em uma fila `f`. Caso esteja, retorna `True`, caso contrário, retorna `False`"""
    esta = False
    aux = []

    while not vazia_fila(f):
        v = retirar(f)
        inserir(aux, v)

        if v == x:
            esta = True  # não pode dar o break, porque senão na hora de voltar os elementos que foram retirados da fila
                         # eles irão para o final e algum elemento do meio passará a ser o primeiro. Ex se tivesse o break:
                         # 1 2 3 4 5 -> 3 4 5 1 2
        

    while not vazia_fila(aux):
        inserir(f, retirar(aux))

    return esta


def inverteFila(f):
    """Inverte o conteúdo de uma fila, usando uma pilha como estrutura de dados auxiliar"""

    p_aux = [] # Meu auxliar será uma pilha
    
    while not vazia_fila(f):
        v = retirar(f)
        funcoes_pilhas.push(p_aux, v)  # Os valores serão invertidos: Na base o primeiro valor da fila e no topo o último valor
    
    while not funcoes_pilhas.vazia(p_aux):
        inserir(f, funcoes_pilhas.pop(p_aux))  # Ao dar o pop, pegaremos os elementos do topo da pilha, ou seja, na ordem inversa que estavam na fila
                                # E, como na fila o primeiro que entra é o primeiro que sai, estaremos invertendo a fila sem maiores complicações4

    print('Invertendo fila...')


def retiraEspecifico(f, x):
    """
    Retira um elemento específico `x` da fila `f`, que será passado como parâmetro da minha função
    Todas as aparições do elemento passado serão removidas
    """

    if not estaNaFila(f, x):
        print(f'O elemento {x} não está na fila passada para a função')

    aux = []
    while not vazia_fila(f):
        v = retirar(f)
        if v != x:
           inserir(aux, v)

    while not vazia_fila(aux):
        inserir(f, retirar(aux))


def analisa_fila(f):
    """Analisa uma fila `f` com números e printa o maior elemento, o menor elemento e a média aritmética dos elementos"""

    aux = []
    maior = float("-inf")
    menor = float("+inf")
    soma = 0
    cont = 0  
    while not vazia_fila(f):
        v = retirar(f)
        # if cont == 0:  # Outra forma de inicializar as variáveis maior e menor
        #     maior = v
        #     menor = v
        cont += 1
        if v > maior:
            maior = v
        if v < menor:
            menor = v
        soma += v
        inserir(aux, v)

    while not vazia_fila(aux):
        inserir(f, retirar(aux))

    print(f'Maior elemento: {maior}')
    print(f'Menor elemento: {menor}')
    media = soma / cont
    print(f'Média aritmética dos elementos: {media}')


