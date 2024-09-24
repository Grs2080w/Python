
# Marca, cor, Potência(Cv), portas
class Carro:
    def __init__(self, marca, cor, potencia, portas):
        self.marca = marca
        self.cor = cor
        self.potencia = potencia
        self.portas = f"{portas} portas"


    def ligar(self):
        print('Girando a chave...')


    def desligar(self):
        print('Girando a chave ao contrário...')


    def porta(self):
        print('Todas as portas fechadas...')


    def exibirInfirmaçõesCarro(self):
        print(self.marca, self.cor, self.potencia, self.portas)


carro1 = Carro('Fiat', 'Vermelho', '100cv', '4')
carro1.ligar()
carro1.desligar()
carro1.porta()
carro1.exibirInfirmaçõesCarro()
