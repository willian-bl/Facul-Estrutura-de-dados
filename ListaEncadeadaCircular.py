"""Lista encadeada circular"""

class ListaCircularNo:
    """
    É um nó da lista. Possui a informação que queremos guardar (`self.info`) e o ponteiro que aponta para o próximo elemento da lista (`self.proximo`) \n
    Quando não possui próximo elemento, `self.info` será `None`
    """

    def __init__(self,info):  # Construtor da classe
        # Em Python, os atributos são públicos por padrão e o uso do self para se referir aos atributos da classe é obrigatório. 
        # Também é obrigatório passar o self como parâmetro de todos os métodos da classe, incluindo o init.
        # Não é necessário colocar ele quando vamos chamar os métodos, mas quando estamos definindo é obrigatório sim.

        self.info=info      # Armazena a informação ou dado
        self.proximo=None   # Armazena o endereço do próximo elemento/nó

    
    # Como os atributos são públicos, não precisava dos getters e setters, mas colocamos para ficar mais semântico e seguir o padrão que estamos usando em Java na disciplina de POO
    def getInfo(self):
        return self.info

    def setInfo(self,info):
        self.info=info

    def getProximo(self):
        return self.proximo

    def setProximo(self,proximo):
        self.proximo=proximo


class ListaLigadaCircular:
    """
    Lista encadeada. É formada por vários nós (Objetos do tipo `ListaCircularNo`). \n
    Seu único atributo é `self.inicio`, que contém o endereço do primeiro nó da lista.
    """

    def __init__(self):
        self.inicio=None  # O único atributo que precisamos para acessar a lista é o endeço do primeiro nó
                          # Sabendo isso, sempre podemos pegar o endereço do próximo nó no nó atual e, assim, a lista pode ser percorrida
                          # A lista acaba quando o endereço do `próximo` no nó atual for None, pois assim não existirá próximo e esse será o último nó


    def insereInicio(self,info):
        """
        Insere um elemento no início da lista encadeada
        `info`: Valor a ser inserido no nó que passará a ser o primeiro da lista encadeada
        """

        no = ListaCircularNo(info)
        if self.inicio == None:  # Se estiver vazia, o nó será o início e referenciará ele mesmo (primeiro da lista). Assim, será uma lista circular de um elemento
            self.inicio = no
            no.proximo = self.inicio
        
        else:  # Se a lista NÃO estiver vazia
            no.proximo = self.inicio  # Fazendo o ponteiro do nó que criamos apontar para aquele que era o primeiro elemento (e que vai passar a ser o segundo)
            
            p = self.inicio
            while p.proximo != self.inicio:  # O fim não será mais None e sim o inicio. Quando o "proximo" do nó for o inicio, quer dizer que este é o último nó
                p = p.proximo
            p.proximo = no  # Alterando o ponteiro próximo do último elemento para o nó que acabamos de criar, que será o primeiro

            self.inicio = no  # Alterando o ponteiro inicio para apontar para o nó que vamos inserir


    def removeInicio(self):
        """Remove o primeiro elemento da lista encadeada"""

        if not self.inicio:  # Verificação para ver se a lista está vazia. Se estiver, inicio será "None" e não tem elemento para remover
            return

        aux=self.inicio  # referencia o primeiro nó 
        if aux.proximo == self.inicio: # Tem apenas um nó, apontando para ele mesmo ou está 
            self.inicio = None

        else:
            while aux.proximo != self.inicio:  # Posicionando o ponteiro no último elemento
                aux = aux.proximo
            
            aux.proximo = self.inicio.proximo  # O último passa a apontar para o segundo elemento
            self.inicio = self.inicio.proximo  # O início passa a apontar para o segundo também. Assim excluímos as referências para o primeiro elemento

            
    def mostraLista(self):
        """Método para printar os elementos da lista encadeada. Printa só os valores armazenados nos nós (não printa os endereços dos próximos elementos)"""

        atual=self.inicio
        if atual == None:
            print("Lista vazia!")
            return

        print("Valores dos nós: ", end='')
        while True:  # Dá certo porque o nó é printado primeiro para depois testar se o atual é igual ao inicio
            print(atual.info, end=' ')
            atual = atual.proximo
            if atual == self.inicio:  # Se for igual, sai do loop
                break
        print()


    def insereDepois(self, p, info):
        """
        Insere um elemento depois de um dado nó \n
        `p`: O nó será inserido depois do nó `p` \n
        `info`: Informação/dado que o que será inserido vai carregar

        Para a lista encadeada circular, não precisa ser alterado. É a mesma função da lista encadeada comum
        """
        
        no = ListaCircularNo(info)
        no.setProximo(p.getProximo())   # Faz com que o ponteiro "próximo" do nó que vamos inserir aponte para o nó depois de "p"
        p.setProximo(no)                # O "p", agora, vai apontar para o nó que inserimos


    def removeDepois(self, p):
        """
        Remove um elemento depois de um dado nó `p`
        Para a lista encadeada circular, não precisa ser alterado. É a mesma função da lista encadeada comum
        """

        aux=p.getProximo()              # aux é o nó que vamos remover
        p.setProximo(aux.getProximo())  # Pegamos o "próximo" do nó que vamos remover e setamos ele como ponteiro "próximo" do nó p
                                        # assim p deixará de referenciar aux e passará a referenciar o nó depois de aux, removendo aux da lista 


    def insereOrdenado(self, x):
        """
        Insere o elemento `x` de forma que a lista sempre fique ordenada em ordem crescente. \n
        Para isso, os valores colocados na lista encadeada devem ser números
        """
        
        p=self.inicio
        if not p or x < p.getInfo():    # Se a lista estiver vazia ou x for menor que o valor do primeiro elemento da lista
            self.insereInicio(x)        # Insere x como primeiro da lista
            return
        
        q = p   # Criamos outro ponteiro para iterar a lista de dois em dois elementos (assim como fizemos no método "removeUltimo")
                # q sempre será o nó a frente de p 

        while q.info < x :    # Enquanto existir o nó q e o dado do nó q for menor que x
            p=q                             # p recebe o ponteiro de q
            q=q.proximo                     # e q recebe o ponteiro do próximo elemento
            if q == self.inicio:
                break

        if q == self.inicio or q.info > x:

            # Se chegamos no último elemento ou se o dado de q é maior que x
            self.insereDepois(p, x)     # Inserimos o nó com o dado x depois de p
                                        # Lembrando que, se entrar no if, q será maior que x e p será menor, pois teremos testado p no loop anterior (os valores de q que são menores que x são passados para p na iteração)
        
        else:  # Se chegar no else, significa que a informação de q é exatamente igual à x. Ou seja, o elemento já foi cadastrado.
            print(f'Elemento anteriormente cadastrado')  # Aqui, nossa tratativa é NÃO adicionar o elemento novamente. Ou seja, trabalhando sempre com o método "insereOrdenado" não teremos elementos repetidos na lista


    def removeOrdenado(self, x):
        """
        Remove o nó com o dado `x` da lista \n
        Para utilizar esta função os valores devem estar ordenados!
        """

        p=self.inicio
        if not p:
            print(f'Lista vazia')
            return

        if p.getInfo()==x:  # O dado que queremos remover é o primeiro da lista
            self.removeInicio()
            return

        # Se a lista não estiver vazia e x não for o primeiro elemento, teremos que percorre-la com dois ponteiros
        q=p
        while q.getInfo() < x:    # É aqui que a condição de que a lista esteja ordenada faz a diferença. Estamos tentando encontrar x não testando se o valor do nó q é igual a x, mas testando se ele é menor do que x
                                        # se for, passamos para o próximo valor. Se não for (q é maior ou igual a x)...
            p=q
            q=q.getProximo()
            if q == self.inicio:
                break

        if q and q.getInfo() == x:        # ... sai do loop e testa se o valor q é igual a x
            self.removeDepois(p)
        else:                           # Se não for igual a x, então q é maior que ele, assim tomamos que o elemento não foi encontrado pois, se a lista está ordenada e o próximo valor é maior, não precisamos mais procurar. Observe que ssas verificações só fazem sentido em uma lista ordenada.
            print(f'elemento nao encontrado')


# Exemplo que pode cair na prova: remover um elemento da lista a partir do final da lista
# Matéria da prova: Fila e Lista encadeada (pilha não vai cair)
# Lista duplamente ligada não vai cair
# Lista circular em si não vai cair tbm, mas o processo de criar a lista circular vai ajudar
# Insere ordenado da lista normal vai cair!!!
