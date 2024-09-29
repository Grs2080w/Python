# Herança e Sobreposição (POO)


class Pessoa():
    Nacionalidade = 'Brasileira'

    ''' A classe 'Pessoa' é a classe Pai, Todos seus Atributos e Funções serão Herdadas
por suas classes filhas.'''

    def __init__(self, nome, cpf, altura):
        self.nome = nome
        self.cpf = cpf
        self.altura = altura


    def Dormir(self):
        print('Dormindo...')


#=====================================================


class Vendedor(Pessoa):
    ' '

    """
    Classe 'Vendedor' é uma das classes filhas, ela recebe Atributos da 
classe 'Pessoa.'
"""
    def __init__(self, NumVend, nome, cpf, altura):
        super().__init__(nome, cpf, altura)
        super().Dormir()
        super().Nacionalidade
        self.NumVend = NumVend

    """
    Super(). chama Atributos e funções da classe Pai.
    Super().__init__ chama os atributos de instância.
    Super().Dormir() chama uma função.
    Super().Nacionalidade chama um atributo de Classe
    
        A partir disso os atributos e funções da classe pai podem ser usados em 
    qualquer lugar dessa classe.
    """


    def InformacoesVend(self):
        print(f'''
Nome: {self.nome}
Cpf: {self.cpf}
Altura: {self.altura}cm
Número de Vendas: {self.NumVend} vendas''')


#=====================================================

# O mesmo vale para essa classe (Classe filha).

class Secretária(Pessoa):
    def __init__(self, id, nome, cpf, altura):
        super().__init__(nome, cpf, altura)
        self.id = id


    def InformacoesSecretária(self):
        print(f'''
Nome: {self.nome}
Cpf: {self.cpf}
Altura: {self.altura}cm
Id: {self.id}''')

# =====================================================

''' 
    Classes filhas também podem ter outras classes filhas, nesse caso a classe 'neta'
irá herdar os atributos e funções da classe Pai e da classe 'Avó'.
'''

class EstagiariaSecre(Secretária):
    Tempo_Estagio = '5 Meses'
    def __init__(self, id, nome, cpf, altura):
        super().__init__( id, nome, cpf, altura)

    def InformacoesEstSec(self):
        print(f'''
Nome: {self.nome}
Cpf: {self.cpf}
Altura: {self.altura}cm
Id: {self.id}
Tempo de Estágio: {EstagiariaSecre.Tempo_Estagio}''')


################################################################################################


v1 = Vendedor('1500', 'João', '08831711393', '163')
s1 = EstagiariaSecre('2', 'Maria', '01431231495', '178')


v1.InformacoesVend()
s1.InformacoesEstSec()

print(' ')

v1.Dormir() # V1 chama função de Pessoa
print(v1.Nacionalidade) # Também chama Atributo de pessoa
