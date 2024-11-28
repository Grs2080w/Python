#Yield

# Em vez de retornar todos os valores de uma vez, um gerador retorna um valor por vez, "suspendendo" sua execução até que o próximo valor seja solicitado. Essa característica é extremamente útil para lidar com grandes conjuntos de dados, pois evita a criação de listas gigantescas na memória, otimizando o uso de recursos.

def ler_csv(nome_arq):
    yield from open('yield/vendas.csv', 'r')
    

vendas = ler_csv("yield/vendas.csv")
# A função iter() transforma um objeto iterável em um iterador.
# Um iterador permite percorrer os elementos do objeto um a um.

for venda in vendas:
   print(venda)