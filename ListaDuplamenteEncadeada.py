class ListaDuplaNo:
    
    def __init__(self, info):
        self.info = info
        self.anterior = None
        self.proximo = None
    
    # No python os atributos são públicos por padrão e, como queremos guardar qualquer tipo de elemento, não criaremos nenhuma restrição 
    # e, por isso, não colocaremos os getters e setters


class ListaDuplaEncadeada:
    
    def __init__(self):
        self.inicio = None
        # Poderíamos ter também um ponteiro self.fim apontando também para o último elemento da lista, para podermos
        # percorrer a lista de trás para frente. Mas, para simplificar, vamos manter apenas o ponteiro inicio
    
    def insereInicio(self, info):
        no = ListaDuplaNo(info)  # Cria um novo nó com o dado passado

        if self.inicio:                 # Caso a lista não esteja vazia, ou seja, existe um nó inicio que era o primeiro elemento...
            no.proximo = self.inicio    # O nó que acabamos de criar, que será o primeiro, irá referenciar o nó que era o primeiro e está no ponteiro inicio
            self.inicio.anterior = no   # Além disso, o anterior do nó inicio deve apontar para o nó que criamos 
        
        self.inicio = no    # Finalmente, atribuímos o endereço do nó que criamos ao ponteiro inicio

    def mostraLista(self):
        atual = self.inicio

        if not atual:
            print('Lista Dupla Encadeada: []')
            return

        s = 'Lista Dupla Encadeada: ['
        while atual:
            s += str(atual.info) + ', '
            atual = atual.proximo
        s = s.rstrip(', ')  # Tirando a vírgula a mais que será colocada depois do último elemento
        s += ']'

        print(s)
    
    def retornaUltimo(self):
        """Retorna o ultimo elemento da lista"""
        
        atual = self.inicio
        if not atual:
            return None  # Deve parar por aqui porque se testar o while atual.proximo, None não tem atributo proximo, então dará erro no código

        while atual.proximo:        # Enquando existe o ponteiro proximo (enquanto ele não é None)
            atual = atual.proximo   # Passa para o próximo elemento

        return atual  # Quando sair do while o atual será o último elemento, que é aquele cujo ponteiro proximo é None
    
    def mostraReverso(self):
        """Mostra os elementos na ordem inversa, usando os ponteiros anterior"""
        
        ultimo = self.retornaUltimo()

        if not ultimo:
            print('Lista Dupla Encadeada Reverso: []')
            return

        s = 'Lista Dupla Encadeada Reverso: ['
        while ultimo:
            s += str(ultimo.info) + ', '
            ultimo = ultimo.anterior
        s = s.rstrip(', ')  # Tirando a vírgula a mais que será colocada depois do último elemento
        s += ']'

        print(s)
    
    def insereDepois(self, p, info):
        novo_no = ListaDuplaNo(info)

        novo_no.proximo = p.proximo     # O proximo do nó que criamos vai apontar para o próximo de p 
        novo_no.anterior = p            # O anterior do nó que criamos vai apontar para p

        p.proximo = novo_no                     # Agora o proximo de p deve apontar para o nó que criamos
        if novo_no.proximo:                     # Se existir um nó depois desse que estamos inserindo
            novo_no.proximo.anterior = novo_no  # O nó seguinte de novo_no (que definimos na linha 77) deve ter o seu ponteiro anterior apontando para o novo_no

    def removeInicio(self):
        aux = self.inicio
        if aux:                                 # Testa se a lista não está vazia
            self.inicio = aux.proximo
            if self.inicio != None:             # Caso tenha só um elemento, vai retirar ele e não vai ter nó no self.inicio, logo 
                self.inicio.anterior = None     # Como é o primeiro elemento, não tem anterior
    
    def removeDepois(self, p):
        no_para_remover = p.proximo
        if no_para_remover:  # Se existir um nó para remover (Sem esse if o código não da erro, mas vai fazer operações desnecessárias)
            p.proximo = no_para_remover.proximo
            if no_para_remover.proximo:
                no_para_remover.proximo.anterior = no_para_remover.anterior



def main():
    # Testando as classes
    lista = ListaDuplaEncadeada()
    lista.insereInicio(10)
    lista.insereInicio(15)
    lista.insereInicio(20)
    lista.mostraLista()
    lista.mostraReverso()

    print()
    # lista.removeInicio()
    # lista.mostraLista()
    # lista.removeInicio()
    # lista.mostraLista()
    lista.removeInicio()
    lista.mostraLista()

    print()
    p = lista.inicio.proximo
    lista.insereDepois(p, 5)
    lista.mostraLista()


if __name__ == '__main__':
    main()

# Tentar fazer um algoritmo para criar uma lista encadeada circular