"""Arquivo com a classe principal de lista encadeada que será usada nas aulas"""

class ListaNo:
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


class ListaLigada:
    """
    Lista encadeada. É formada por vários nós (Objetos do tipo `ListaNo`). \n
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

        no=ListaNo(info)            # Cria um novo nó com o dado passado
        no.setProximo(self.inicio)  # O ponteiro "próximo" do nó passará a apontar para aquele que era o primeiro elemento da lista e cujo ponteiro estava guardado em self.inicio
        self.inicio=no              # E o início passará a apontar para o nó que criamos, que agora será o primeiro. 
        # Essa última atribuição faz com que self.inicio receba o endereço/referência do objeto "nó" e NÃO é uma cópia do objeto nó. 
        # É só lembrar dos conceitos trabalhados em POO. Os objetos são manipulados, passados como parâmetros em funções e atriubuidos através de seus endereços na memória


    def removeInicio(self):
        """Remove o primeiro elemento da lista encadeada"""

        aux=self.inicio  # self.inicio referencia o primeiro nó
        if aux:  # Verificação para ver se a lista não está vazia. Se estiver, inicio será "None" e não tem elemento para remover
            self.inicio=aux.getProximo()  # Simplesmente atribuímos o endereço do segundo nó (que foi pego do atributo "proximo" do primeiro nó) ao "inicio"
        
        """Conceito novo: Coletor de lixo"""
        # IMPORTANTE
        # Uma coisa interessante que acontece aqui é que se existir o primeiro nó, o atributo que o referenciava ("inicio") deixará de referenciar ele. Ou seja, depois de executada a função, o primeiro nó
        # não terá mais nenhuma variável que o referencie. Nas linguagens de programação existe algo chamado "coletor de lixo" e, em Python, a coleta de lixo acontece automaticamente.
        # O coletor de lixo (ou "garbage collector") é o responsável por gerenciar os recursos de memória e fazer a liberação de memória de uma forma automática.
        # Isso é importante para evitar que o programa utilize mais memória do que o necessário ou que ocorra vazamento de memória (memory leak).
        # De tempos em tempos, o coletor de lixo identifica objetos que não tem mais nenhum ponteiro apontando para eles e limpa o endereço de memória correspondente, liberando recursos do computador que está rodando o programa.
        # Em algumas linguagens, isso não é feito automaticamente, então o programador deve perceber quando uma variável está ficando sem um ponteiro e limpar o endereço de memória manualmente.


    def existeElemento(self, x):
        """Procura se um elemento `x` existe na lista encadeada."""

        p=self.inicio
        encontrou=False
        while p and not encontrou:  # Enquanto existir um nó no ponteiro p e ainda não tiver encontrado o valor na lista
            if x == p.getInfo():
                encontrou=True
            p=p.getProximo()  # p passa a referenciar o próximo elemento da lista

        return encontrou


    def mostraLista(self):
        """Método para printar os elementos da lista encadeada. Printa só os valores armazenados nos nós (não printa os endereços dos próximos elementos)"""

        atual=self.inicio
        print("Valores dos nós: ", end='')
        while atual:
            # print(f'Valor no: {atual.getInfo()}')  # Print do professor. Alterei deixando mais interessante para mim
            print(atual.getInfo(), end=' ')
            atual=atual.getProximo()
        print()


    def contaNoLista(self, printar=True):
        """Conta a quantidade de nós existentes na lista encadeada. Printa a lista (se `printar` for `True`) e retorna essa quantidade"""

        atual=self.inicio
        cont=0
        while atual:
            cont += 1
            atual = atual.getProximo()
        
        if printar:
            print(f'Tamanho da lista: {cont}')

        return cont


    def insereUltimo(self, info):
        """
        Insere um valor como último nó da lista encadeada \n
        `info`: Valor a ser inserido no nó que passará a ser o último da lista encadeada
        """

        atual=self.inicio
        if not atual:                   # Se a lista não tiver um início, ou seja, se não tiver nenhum valor
            self.insereInicio(info)     # O elemento será inserido no início, como primeiro elemento mesmo
            return
        
        while atual.getProximo():       # Enquanto existir um próximo nó
            atual=atual.getProximo()    # Continua iterando pela lista

        # Quando não existir um próximo nó, significa que este é o último nó da lista
        no = ListaNo(info)      # Cria um novo nó com o elemento passado como parâmetro
        atual.setProximo(no)    # O ponteiro "próximo" daquele que era o último nó é alterado para apontar para o novo nó (que será o último) 


    def removeUltimo(self):
        """Remove o último valor de uma lista encadeada"""

        # Usa dois ponteiros, p e q. 
        p=None
        q=self.inicio
        if not q:
            print(f'Lista vazia')
            return

        while q.getProximo():   # Enquanto o elemento q tiver um próximo elemento
            p=q                 # p recebe o ponteiro de q
            q=q.getProximo()    # e q recebe o ponteiro do próximo elemento
        # basicamente, nesse while, os ponteiros p e q vão percorrer a lista, sendo sempre q o ponteiro do nó a frente de p
        # quando o while acabar, significa que q não tem um próximo nó. Ou seja, q será o último elemento da lista e p o penúltimo.
        # assim, o nó que teremos que remover será o q. Precisamos do p porque temos que editar a referência do próximo nó nele, removendo a referência do nó de q
        
        if p==None:             # Significa que só existe um nó
            self.inicio=None    # Então ele mesmo será removido, retirando a referência do ponteiro do início da lista
        else:
            p.setProximo(None)  # Se existe um nó em p, então para remover o nó q retiramos a referência desse nó em p


    def insereDepois(self, p, info):
        """
        Insere um elemento depois de um dado nó \n
        `p`: O nó será inserido depois do nó `p` \n
        `info`: Informação/dado que o que será inserido vai carregar
        """
        
        no = ListaNo(info)
        no.setProximo(p.getProximo())   # Faz com que o ponteiro "próximo" do nó que vamos inserir aponte para o nó depois de "p"
        p.setProximo(no)                # O "p", agora, vai apontar para o nó que inserimos


    def removeDepois(self, p):
        """Remove um elemento depois de um dado nó `p`"""

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

        while q and q.getInfo() < x :   # Enquanto existir o nó q e o dado do nó q for menor que x
            p=q                         # p recebe o ponteiro de q
            q=q.getProximo()            # e q recebe o ponteiro do próximo elemento

        if not q or q.getInfo() > x :   # Se chegamos no último elemento (p é o último e não existe q) ou se o dado de q é maior que x
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
        while q and q.getInfo() < x:    # É aqui que a condição de que a lista esteja ordenada faz a diferença. Estamos tentando encontrar x não testando se o valor do nó q é igual a x, mas testando se ele é menor do que x
                                        # se for, passamos para o próximo valor. Se não for (q é maior ou igual a x)...
            p=q
            q=q.getProximo()

        if q and q.getInfo()==x:        # ... sai do loop e testa se o valor q é igual a x
            self.removeDepois(p)
        else:                           # Se não for igual a x, então q é maior que ele, assim tomamos que o elemento não foi encontrado pois, se a lista está ordenada e o próximo valor é maior, não precisamos mais procurar. Observe que ssas verificações só fazem sentido em uma lista ordenada.
            print(f'elemento nao encontrado')

