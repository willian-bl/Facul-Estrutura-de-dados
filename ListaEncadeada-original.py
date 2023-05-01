"""Classe original do professor, sem os comentários"""

class ListaNo:

    def __init__(self,info):
        self.info=info
        self.proximo=None

    def getInfo(self):
        return self.info

    def setInfo(self,info):
        self.info=info

    def getProximo(self):
        return self.proximo

    def setProximo(self,proximo):
        self.proximo=proximo


class ListaLigada:

    def __init__(self):
        self.inicio=None

    def insereInicio(self,info):
        no=ListaNo(info)
        no.setProximo(self.inicio)
        self.inicio=no

    def removeInicio(self):
        aux=self.inicio
        if aux:
            self.inicio=aux.getProximo()


    def existeElemento(self,x):
        p=self.inicio
        encontrou=False
        while p and not encontrou:
            if x == p.getInfo():
                encontrou=True
            p=p.getProximo()

        return encontrou


    def mostraLista(self):
        atual=self.inicio
        while atual:
            print(f'Valor no: {atual.getInfo()}')
            atual=atual.getProximo()


    def contaNoLista(self):
        atual=self.inicio
        cont=0
        while atual:
            cont=cont+1
            atual=atual.getProximo()

        print(f'Tamanho da lista: {cont}')


    def insereUltimo(self,info):
        atual=self.inicio
        if not atual:
            self.insereInicio(info)
            return
        while atual.getProximo():
            atual=atual.getProximo()
        no = ListaNo(info)
        atual.setProximo(no)

    def removeUltimo(self):
        p=None
        q=self.inicio
        if not q:
            print(f'lista vazia')
            return

        while q.getProximo():
            p=q
            q=q.getProximo()

        if p==None:
            self.inicio=None
        else:
            p.setProximo(None)


    def insereDepois(self,p,info):
        no = ListaNo(info)
        no.setProximo(p.getProximo())
        p.setProximo(no)

    def removeDepois(self,p):
        aux=p.getProximo()
        p.setProximo(aux.getProximo())


    def insereOrdenado(self,x):
        p=self.inicio
        if not p or x < p.getInfo():
            self.insereInicio(x)
            return
        q = p

        while q and q.getInfo() < x :
            p=q
            q=q.getProximo()

        if not q or q.getInfo() >x :
            self.insereDepois(p,x)
        else:
            print(f'Elemento anteriormente cadastrado')

    def removeOrdenado(self,x):
        p=self.inicio
        if not p:
            print(f'lista vazia')
            return

        if p.getInfo()==x:
            self.removeInicio()
            return

        q=p
        while q and q.getInfo() < x:
            p=q
            q=q.getProximo()

        if q and q.getInfo()==x:
            self.removeDepois(p)
        else:
            print(f'elemento nao encontrado')

