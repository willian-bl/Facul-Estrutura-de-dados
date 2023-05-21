"""
Trabalho de listas encadeadas - Lista encadeada de alunos e disciplinas

Leandro Guilhermiti de Oliveira
Willian Brito de Lima
"""

class ListaNoDisciplina:
    """Nó da lista de disciplinas"""

    def __init__(self, codigo, nome, frequencia, nota):
        self.codigo = codigo
        self.nome = nome
        self.frequencia = frequencia
        self.nota = nota
        self.proximo = None


    def getCodigo(self):
        return self.codigo

    def setCodigo(self, codigo):
        self.codigo = codigo
    
    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome
    
    def getFrequencia(self):
        return self.frequencia

    def setFrequencia(self, frequencia):
        self.frequencia = frequencia

    def getNota(self):
        return self.nota

    def setNota(self, nota):
        self.nota = nota


    def getProximo(self):
        return self.proximo

    def setProximo(self, proximo):
        self.proximo = proximo


class ListaLigadaDisciplina:
    """Lista ligada de disciplinas"""

    def __init__(self):
        self.inicio = None


    def insereInicio(self, codigo, nome, frequencia, nota):
        no = ListaNoDisciplina(codigo=codigo, nome=nome, frequencia=frequencia, nota=nota)
        no.setProximo(self.inicio)
        self.inicio = no

    def insereUltimo(self, codigo, nome, frequencia, nota):
        atual=self.inicio

        if not atual:
            self.insereInicio(codigo, nome, frequencia, nota)
            return
        
        while atual.getProximo():
            atual=atual.getProximo()

        no = ListaNoDisciplina(codigo, nome, frequencia, nota)
        atual.setProximo(no)

    def insereDepois(self, p, codigo, nome, frequencia, nota):
        no = ListaNoDisciplina(codigo, nome, frequencia, nota)
        
        no.setProximo(p.getProximo())
        p.setProximo(no)
    
    def insereOrdenado(self, codigo, nome, frequencia, nota):
        """Insere o elemento de forma que a lista sempre fique ordenada em ordem crescente de acordo com o codigo da disciplina"""
        
        # Se a lista estiver vaiza ou se codigo for menor que o do primeiro da lista, insere no início
        p=self.inicio
        if not p or codigo < p.getCodigo():
            self.insereInicio(codigo, nome, frequencia, nota)
            return
        
        q = p

        while q and q.getCodigo() < codigo :
            p=q
            q=q.getProximo()

        if not q or q.getCodigo() > codigo :  # Proximo é maior, então insere depois de p. (ou ele é maior que todos e vai ser inserido como último elemento)
            self.insereDepois(p, codigo, nome, frequencia, nota)
        else:  # Se já existir um elemento com o mesmo codigo
            print(f'Já existe uma disciplina com esse codigo cadastrada para esse aluno!')
    

    def removeInicio(self):
        aux=self.inicio
        if aux:
            self.inicio=aux.getProximo()

    def removeUltimo(self):
        p=None
        q=self.inicio
        if not q:
            print(f'Não tem alunos na lista!')
            return

        while q.getProximo():
            p=q
            q=q.getProximo()

        if p==None:             # Significa que só existe um nó
            self.inicio=None    # Então ele mesmo será removido, retirando a referência do ponteiro do início da lista
        else:
            p.setProximo(None)  # Se existe um nó em p, então para remover o nó q retiramos a referência desse nó em p
    
    def removeDepois(self, p):
        aux=p.getProximo()              # aux é o nó que vamos remover
        p.setProximo(aux.getProximo())  # Pegamos o "próximo" do nó que vamos remover e setamos ele como ponteiro "próximo" do nó p
                                        # assim p deixará de referenciar aux e passará a referenciar o nó depois de aux, removendo aux da lista 

    def removeOrdenado(self, codigo):
        p=self.inicio
        if not p:
            print(f'Lista sem disciplinas!')
            return

        if p.getCodigo()==codigo:  # O dado que queremos remover é o primeiro da lista
            self.removeInicio()
            return

        # Se a lista não estiver vazia e codigo não for o primeiro elemento, teremos que percorre-la com dois ponteiros
        q=p
        while q and q.getCodigo() < codigo:   # É aqui que a condição de que a lista esteja ordenada faz a diferença. Estamos tentando encontrar codigo não testando se o valor do nó q é igual a codigo, mas testando se ele é menor do que codigo
                                        # se for, passamos para o próximo valor. Se não for (q é maior ou igual a codigo)...
            p=q
            q=q.getProximo()

        if q and q.getCodigo()==codigo:        # ... sai do loop e testa se o valor q é igual a codigo
            self.removeDepois(p)
        else:                           # Se não for igual a codigo, então q é maior que ele, assim tomamos que o elemento não foi encontrado pois, se a lista está ordenada e o próximo valor é maior, não precisamos mais procurar. Observe que essas verificações só fazem sentido em uma lista ordenada.
            print(f'Disciplina não encontrada')


    def alteraDisciplina(self, codigo, nome, frequencia, nota):
        disciplina_atual = self.inicio

        if not disciplina_atual:
            print('Esse aluno não tem nenhuma disciplina para ser alterada.')
            return
        
        while disciplina_atual:
            if disciplina_atual.getCodigo() == codigo:
                disciplina_atual.setNome(nome)
                disciplina_atual.setFrequencia(frequencia)
                disciplina_atual.setNota(nota)
                return

            disciplina_atual = disciplina_atual.getProximo()
        
        print('Disciplina não encontrada')


    def mostraLista(self):
        atual=self.inicio

        print('Disciplinas: ')
        if not atual:
            print('Esse aluno não está matriculado em nenhuma disciplina.')
            return
        
        while atual:
            print(f'Codigo: {atual.getCodigo()} -> Disciplina: {atual.getNome()}, Frequência: {atual.getFrequencia()}, Nota: {atual.getNota()}')
            atual=atual.getProximo()


class ListaNoAluno:
    """Nó da lista de alunos"""

    def __init__(self, rgm, nome, endereco, curso):  
        self.rgm = rgm
        self.nome = nome
        self.endereco = endereco
        self.curso = curso
        self.proximo = None  
        self.disciplinas = ListaLigadaDisciplina()  # Criando um ponteiro início para a lista de disciplinas


    def setRGM(self, rgm):
        self.rgm = rgm

    def getRGM(self):
        return self.rgm
    
    def setNome(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome
    
    def setEndereco(self, endereco):
        self.endereco = endereco

    def getEndereco(self):
        return self.endereco
        
    def setCurso(self, curso):
        self.curso = curso

    def getCurso(self):
        return self.curso


    def setProximo(self,proximo):
        self.proximo=proximo

    def getProximo(self):
        return self.proximo


class ListaLigadaAlunos:
    "Lista ligada de alunos"

    def __init__(self):
        self.inicio=None


    def insereInicio(self, rgm, nome, endereco, curso):
        no = ListaNoAluno(rgm=rgm, nome=nome, endereco=endereco, curso=curso)
        no.setProximo(self.inicio)
        self.inicio = no

    def insereUltimo(self, rgm, nome, endereco, curso):
        atual=self.inicio

        if not atual:
            self.insereInicio(rgm, nome, endereco, curso)
            return
        
        while atual.getProximo():
            atual=atual.getProximo()

        no = ListaNoAluno(rgm, nome, endereco, curso)
        atual.setProximo(no)

    def insereDepois(self, p, rgm, nome, endereco, curso):
        no = ListaNoAluno(rgm, nome, endereco, curso)
        
        no.setProximo(p.getProximo())
        p.setProximo(no)
    
    def insereOrdenado(self, rgm, nome, endereco, curso):
        """Insere o elemento de forma que a lista sempre fique ordenada em ordem crescente de acordo com o RGM do aluno"""
        
        # Se a lista estiver vaiza ou se rgm for menor que o do primeiro da lista, insere no início
        p=self.inicio
        if not p or rgm < p.getRGM():
            self.insereInicio(rgm, nome, endereco, curso)
            return
        
        q = p

        while q and q.getRGM() < rgm :
            p=q
            q=q.getProximo()

        if not q or q.getRGM() > rgm :  # Proximo é maior, então insere depois de p. (ou ele é maior que todos e vai ser inserido como último elemento)
            self.insereDepois(p, rgm, nome, endereco, curso)
        else:  # Se já existir um elemento com o mesmo RGM
            print(f'Já existe um aluno com esse RGM!')
    

    def removeInicio(self):
        aux=self.inicio

        if aux.disciplinas:
            print('Não é possível remover o aluno, pois ele possui disciplinas')
            return

        if aux:
            self.inicio=aux.getProximo()

    def removeUltimo(self):
        p=None
        q=self.inicio
        if not q:
            print(f'Não tem alunos na lista!')
            return

        while q.getProximo():
            p=q
            q=q.getProximo()

        if q.disciplinas:
            print('Não é possível remover o aluno, pois ele possui disciplinas')
            return

        if p==None:             # Significa que só existe um nó
            self.inicio=None    # Então ele mesmo será removido, retirando a referência do ponteiro do início da lista
        else:
            p.setProximo(None)  # Se existe um nó em p, então para remover o nó q retiramos a referência desse nó em p
    
    def removeDepois(self, p):
        aux=p.getProximo()              # aux é o nó que vamos remover
        if aux.disciplinas:
            print('Não é possível remover o aluno, pois ele possui disciplinas')
            return

        p.setProximo(aux.getProximo())  # Pegamos o "próximo" do nó que vamos remover e setamos ele como ponteiro "próximo" do nó p
                                        
    def removeOrdenado(self, rgm):
        p=self.inicio
        if not p:
            print(f'Lista sem alunos!')
            return

        if p.getRGM()==rgm:  # O dado que queremos remover é o primeiro da lista
            self.removeInicio()
            return

        # Se a lista não estiver vazia e rgm não for o primeiro elemento, teremos que percorre-la com dois ponteiros
        q=p
        while q and q.getRGM() < rgm:   # É aqui que a condição de que a lista esteja ordenada faz a diferença. Estamos tentando encontrar rgm não testando se o valor do nó q é igual a rgm, mas testando se ele é menor do que rgm
                                        # se for, passamos para o próximo valor. Se não for (q é maior ou igual a rgm)...
            p=q
            q=q.getProximo()

        if q and q.getRGM()==rgm:        # ... sai do loop e testa se o valor q é igual a rgm
            self.removeDepois(p)
        else:                           # Se não for igual a rgm, então q é maior que ele, assim tomamos que o elemento não foi encontrado pois, se a lista está ordenada e o próximo valor é maior, não precisamos mais procurar. Observe que essas verificações só fazem sentido em uma lista ordenada.
            print(f'Aluno não encontrado')


    def obtemListaDisciplina(self, rgm):
        p=self.inicio
        while p:
            if p.getRGM() == rgm:
                return p.disciplinas
        
            p = p.proximo

        return None
    
    def cadastraDisciplina(self, rgm, codigo, nome, frequencia, nota):
        dis = self.obtemListaDisciplina(rgm)
        if dis:
            dis.insereOrdenado(codigo, nome, frequencia, nota)
        else:
            print('Aluno não encontrado')
    
    def alteraDisciplinaDoAluno(self, rgm, codigo, nome, frequencia, nota):
        dis = self.obtemListaDisciplina(rgm)
        if dis:
            dis.alteraDisciplina(codigo, nome, frequencia, nota)
        else:
            print('Aluno não encontrado')


    def alteraAluno(self, rgm, nome, endereco, curso):
        aluno_atual = self.inicio

        if not aluno_atual:
            print('Lista de alunos está vazia')
            return

        while aluno_atual:
            if aluno_atual.getRGM() == rgm:
                aluno_atual.setNome(nome)
                aluno_atual.setEndereco(endereco)
                aluno_atual.setCurso(curso)
                return
            
            aluno_atual = aluno_atual.getProximo()
        
        print('Aluno não encontrado')


    def mostraAlunos(self):
        atual=self.inicio

        if not atual:
            print('Não tem nenhum aluno na lista!')
            return

        print('------ Alunos na lista: ------')
        while atual:
            print(f'\nRGM: {atual.getRGM()} | Nome: {atual.getNome()} \nCurso: {atual.getCurso()} | Endereço: {atual.getEndereco()}')
            dis = atual.disciplinas
            dis.mostraLista()

            atual=atual.getProximo()

    def mostraReprovados(self):
        aluno_atual = self.inicio

        print('\nAlunos reprovados em ao menos uma disciplina: ')
        while aluno_atual:
            dis = aluno_atual.disciplinas
            
            disciplina_atual = dis.inicio
            while disciplina_atual:
                if disciplina_atual.getNota() < 6:
                    print(f'\nRGM: {aluno_atual.getRGM()} | Nome: {aluno_atual.getNome()} \nCurso: {aluno_atual.getCurso()} | Endereço: {aluno_atual.getEndereco()}')
                    break
                disciplina_atual = disciplina_atual.getProximo()

            aluno_atual = aluno_atual.getProximo()

    def mostraAprovados(self):
        aluno_atual = self.inicio

        print('\nAlunos aprovados em todas as disciplinas: ')
        while aluno_atual:
            dis = aluno_atual.disciplinas
            
            disciplina_atual = dis.inicio
            reprovado = False
            while disciplina_atual:
                if disciplina_atual.getNota() < 6:
                    reprovado = True
                    break
                disciplina_atual = disciplina_atual.getProximo()
            
            if not reprovado:
                print(f'\nRGM: {aluno_atual.getRGM()} | Nome: {aluno_atual.getNome()} \nCurso: {aluno_atual.getCurso()} | Endereço: {aluno_atual.getEndereco()}')

            aluno_atual = aluno_atual.getProximo()

# ----------- Teste das classes -----------------
def main():
    cad_alunos = ListaLigadaAlunos()
    cad_alunos.insereOrdenado(rgm=13, nome="João", endereco="Rua dos Coqueiros", curso="Análise e Desenvolvimento de Sistemas")
    cad_alunos.insereOrdenado(rgm=12, nome="Ana", endereco="Rua das Oliveiras", curso="Sistemas da Informação")

    cad_alunos.cadastraDisciplina(12, 1, 'Estrutura de dados', 70, 8)
    cad_alunos.cadastraDisciplina(12, 2, 'POO', 85, 7)
    cad_alunos.cadastraDisciplina(12, 3, 'Matemática discreta', 40, 5.5)

    cad_alunos.cadastraDisciplina(13, 3, 'Matemática discreta', 80, 7.5)

    cad_alunos.mostraAlunos()
    cad_alunos.mostraAprovados()
    cad_alunos.mostraReprovados()

    print('\nTentando remover o primeiro aluno da lista:')
    cad_alunos.removeInicio()

if __name__ == '__main__':
    main()
