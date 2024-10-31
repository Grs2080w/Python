from googletrans import Translator

# Criar um objeto tradutor
translator = Translator()


# Função para traduzir texto
def traduzir_texto():
    texto = """"""
    print("Digite o texto que deseja traduzir para o português (digite 'sair' para encerrar):")

    while True:
        linha = input()
        if linha.lower() == 'sair':
            break
        texto += linha + "\n"  # Adiciona nova linha ao texto

    # Traduzir o texto
    traducao = translator.translate(texto, dest='pt')

    # Exibir a tradução
    print("\nTexto traduzido para português:")
    print(traducao.text)


# Chamar a função
traduzir_texto()


# DO by chatGpt