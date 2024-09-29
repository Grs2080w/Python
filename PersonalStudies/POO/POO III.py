from PersonalStudies.POO.POOIIIA import Conta


rodrigo = Conta('Rodrigo Alves', '088.317.113-93', '6589-98-9876', 1489.00)

"""Como indicado no documento 'POOIIIA' se o saldo for menor que 0, ele retorna um print, e não adiciona
o valor, se for maior, atualiza o valor"""

rodrigo.set_saldo(1500) # Seta o valor da conta como 1500

rodrigo.set_Sacar(20) # Faz o cálculo e mostra o saldo apos o saque

rodrigo.InfoConta()

rodrigo.set_deposita(30)

rodrigo.InfoConta()

