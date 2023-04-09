"""Arquivo com funções usadas para manipulação de pilhas. Conforme novas funções forem sendo criadas durante as aulas, elas serão adicionadas aqui para serem importadas em outros projetos"""

# ------------------------------ FUNÇÕES PRIMITIVAS ------------------------------
def push(p, v):
    """Coloca um valor no topo da pilha"""
    # p representa a pilha (utilizamos uma lista para representar) e v o valor a ser inserido
    p.append(v)


def pop(p):
    """Retira um valor do topo da pilha"""
    return p.pop()


def vazia(p):
    """Verifica se a pilha está vazia ou não. Caso esteja, retorna `True`"""
    return False if p else True

# ------------------------------ FUNÇÕES COMPLEMENTARES ------------------------------
def mostraPilha(p):
    """
    A função mostrapilha tem como objetivo mostrar o conteudo da \n
    pilha p (passada como parâmetro) utilizando as funções primitivas \n
    para manipulação de pilha.
    """

    if vazia(p):
        print('Pilha vazia!')
        return

    aux = [] # Para a elaboração da função precisa-se de uma pilha auxiliar
    while not vazia(p): # enquanto a pilha p não estiver vazia
        v = pop(p) # retirar o elemento do topo da pilha P
        push(aux, v) # colocar o elemento na pilha auxiliar
    
    while not vazia(aux):   # retornar os elementos da pilha auxiliar
        v = pop(aux)        # para a pilha P
        print(v)            # mostrar os elementos na ordem de inserção
        push(p, v)


def quantidadePilha(p):
    """
    A função quantidadePilha tem como objetivo contar a quantidade de valores armazenados \n
    em uma pilha p (passada como parâmetro) utilizando as funções primitivas \n
    para manipulação de pilha e mantendo os elementos na pilha original
    """

    aux = [] # Para a elaboração da função precisa-se de uma pilha auxiliar
    qe = 0  # E de um contador
    while not vazia(p): # enquanto a pilha p não estiver vazia
        v = pop(p) # retirar o elemento do topo da pilha P
        push(aux, v) # colocar o elemento na pilha auxiliar
    
    while not vazia(aux):   # retornar os elementos da pilha auxiliar
        v = pop(aux)        # para a pilha P
        qe += 1      # e contar os elementos equanto isso é feito
        push(p, v)
    
    return qe


def retiraPrimeiro(p):
    """
    Função para retirar o primeiro valor inserido em uma pilha \n
    Passa todos os elementos para uma pilha auxiliar, depois dá um pop nessa pilha \n
    e retorna os elementos restantes para a pilha, sem o primeiro.
    """
    
    aux = []
    
    if vazia(p):  # Verifica se a pilha está vazia, pois se estiver não tem nada para retirar
        print('Pilha vazia')
        return

    while not vazia(p):     # Coloca os elementos da pilha p em uma pilha auxiliar, pois assim os elementos na pilha auxiliar
        push(aux, pop(p))   # estarão na ordem inversa aos da pilha p, sendo que o primeiro elemento colocado em p será o elemento
                            # do topo de aux, ao qual temos acesso.
    
    primeiro = pop(aux)  # Agora, retira o elemento do topo da pilha auxiliar

    while not vazia(aux):   # Por fim, retornamos os elementos de auxiliar para p, mas sem o primeiro valor, que demos
        push(p, pop(aux))   # o pop antes
        
    return primeiro


def copiaPilha(p1, p2):
    """Função que faz uma cópia idêntica de uma pilha para outra, com os elementos na mesma ordem que foram inseridos na pilha original"""

    aux = []

    while not vazia(p1):  # Retira os elementos da pilha p1 e coloca na pilha auxiliar
        push(aux, pop(p1))

    while not vazia(aux):  
        v = pop(aux)    # Agora, retira os elementos da pilha auxiliar e coloca
        push(p1, v)     # tanto na pilha p1
        push(p2, v)     # quanto na pilha p2


def pilhas_iguais(p1, p2):
    """
    Compara duas pilhas e retorna True caso elas sejam iguais. \n
    Só retornará True caso as pilhas tenham o mesmo tamanho e os mesmos elementos na mesma ordem.
    """
    
    if quantidadePilha(p1) != quantidadePilha(p2):  # Se o tamanho das pilhas não for igual, não precisamos nem comparar,
        return False                                # já retornamos false e não fazemos o resto

    # Caso o tamanho das pilhas seja igual, fazemos as comparações
    p_aux1, p_aux2 = [], []
    eh_igual = True  # Começamos assumindo que as pilhas são iguais 

    # Comparando os valores
    while not vazia(p1):  # Como as pilhas tem tamanho igual, quando os elementos da pilha 1 se esgotarem, os da pilha 2 também terão se esgotado
        
        # Retira das pilhas originais
        v1 = pop(p1)
        v2 = pop(p2)

        # Coloca nas pilhas auxiliares
        push(p_aux1, v1)
        push(p_aux2, v2)

        if v1 != v2:            # Caso o valor retirado de uma pilha seja diferente do valor retirado da outra, as pilhas não são iguais
            eh_igual = False    # Mudamos o valor do flag, que foi definido como True por padrão
            break               # Não precisamos comparar mais
    
    # Retornando valores para as pilhas originais
    while not vazia(p_aux1):
        
        # Retira das pilhas auxiliares
        v1 = pop(p_aux1)
        v2 = pop(p_aux2)

        # Coloca nas pilhas originais
        push(p1, v1)
        push(p2, v2)
    
    return eh_igual


