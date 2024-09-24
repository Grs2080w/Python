# Class
# Syntax
# Marca, Memoria Ram, Placa de Vídeo
class Compultador:
    def __init__(self, marca, memoria_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video

    def Ligar(self):
        print('Estou ligando...')

    def Desligar(self):
        print('Estou desligando...')


    def ExibirinformacoesDesteCompultador(self):
        print(self.marca, self.memoria_ram, self.placa_de_video)
    pass


compultador1 = Compultador('Asus', '8gb', 'Nvidia')
compultador1.Ligar()
compultador1.ExibirinformacoesDesteCompultador()
compultador1.Desligar()


