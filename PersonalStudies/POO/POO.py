# Atributos de Classes/Instâncias, Métodos, Decorators de Classes (POO)

class Empregado:
    Ocupação = 'Ativo'

    """Atributo de Classe -> Vale pra todos da classe
    Todas as 'Pessoas' estarão no estado de Funcionário, TODOS. """


    # Atributos de Instâncias / Características
    def __init__(self, nome, altura, peso, idade, sexo, cpf, cargo):

        self.nome = nome
        self.altura = altura
        self.peso = peso
        self.idade = idade
        self.sexo = str(sexo)
        self.cpf = cpf
        self.cargo = cargo


    # ==================== Métodos / Ações ====================


    def Dormir(self):
        print(f'Fechando os olhos...')

    def Descansar(self):
        print("Descançando...")

    def Trabalhar(self):
        print("Trabalhando...")

    def Rindo(self):
        print("Almoçando...")

    def InformaçõesDoEmpregado(self):
        print(" ")
        print(f'''
Ocupação: {self.Ocupação}
Nome: {self.nome}
Altura: {self.altura} Cm
Idade: {self.idade} Anos
Peso: {self.peso} Kgs
Sexo: {self.sexo}
Cpf: {self.cpf}
Cargo: {self.cargo}''')
        print(" ")

    @classmethod
    def AlterarOcupação(cls, ocupação):
        Empregado.Ocupação = ocupação


    @classmethod
    def ExibirCargo(cls):
        print(f'Situação das Ocupações: {Empregado.Ocupação}')


    @staticmethod
    def jovemAprendiz(idade):
        if idade < 18:
            print('Não tem direito a Jovem Aprendiz :(')
        else:
            print('Tem direito a Jovem Aprendiz :)')


''' @CLASSMETHOD Converte uma função para um Método de classe, ou seja, agora pode ser usado como
parâmetro da função, um dos atributo da própria classe. Dessa forma, funções da classe podem retornar,
alterar valores de atributos da própria classe. 
    Toda função com @CLASSMETHOD recebe como parâmetro um 'CLS' indicando que o argumento está 
presente nos Atributos de Classe.'''

''' @STATICMETHOD Faz com que a função não tenha acesso a nenhum Atributo de Classe nem de de instância,
fazendo dela uma função normal dentro da classe. Usada normalmente para coisas banais.'''


###############################################################################################################################################################



gabriel = Empregado('Gabriel Santos', 1.65, 70, 16,
                    'Masculino', '08831711393', 'Soldador')
Letícia = Empregado('Letícia Gonzaga', 1.60, 50, 16,
                    'Feminino', '89564732198', 'Gerente de Rh')


Empregado.AlterarOcupação('Demitido')
""" Perceba que aqui ocupação é igual 'Demitido', sendo uma alteração no 
atributo de classe, de todas os componentes daquela classe"""

Empregado.ExibirCargo()

gabriel.InformaçõesDoEmpregado()
Letícia.InformaçõesDoEmpregado()

print('=-' * 50)

Empregado.AlterarOcupação('Ativo')
"""Aqui Ocupação = Readmitido, sendo o valor que realmente conta
já que foi o ultimo"""

Empregado.ExibirCargo()

gabriel.InformaçõesDoEmpregado()
Letícia.InformaçõesDoEmpregado()

print('=-' * 50)

Empregado.AlterarOcupação('Readmitido')
"""Aqui Ocupação = Readmitido, sendo o valor que realmente conta
já que foi o ultimo"""

Empregado.ExibirCargo()

gabriel.InformaçõesDoEmpregado() # Aqui vemos de fato a Ocupação = 'Readmitido' nos dois Componentes
Letícia.InformaçõesDoEmpregado()


print('=-' * 50)


Empregado.jovemAprendiz(18)


