class Cliente():
    def __init__(self, nome, cpf):
        self._nome = nome
        self._cpf = cpf # '_' antes do nome dá mais segurança


class Conta(Cliente):
    def __init__(self, nome, cpf, __numeroCont, __saldo):
        super().__init__(nome, cpf)
        self.__numeroCont = __numeroCont
        self.__saldo = __saldo


    def InfoConta(self):
        print(f'''
Nome: {self._nome}
CPF: {self._cpf}
Número da Conta: {self.__numeroCont}
Saldo: R${self.__saldo}
''')
    #Metodo get
    def get_nome(self):
        return self._nome


    #Metodo set
    def set_saldo(self, saldo):
        if saldo < 0:
            print('Saldo não pode ser negativo')
        else:
            self.__saldo = saldo


    def set_Sacar(self, saque):
        self.__saldo = self.__saldo - saque


    def set_deposita(self, depo):
        self.__saldo = self.__saldo + depo
