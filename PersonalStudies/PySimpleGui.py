from PySimpleGUI import PySimpleGUI as sg
from myThings import manipText
from myThings.manipText import *

loginex = arquivoExiste('Logins.txt')
senhaex = arquivoExiste('Senhas.txt')
if not loginex or  not senhaex:
    manipText.criarArq('Logins.txt')
    manipText.criarArq('Senhas.txt')


loginsdad = open('Logins.txt', 'r')
senhasdad = open('Senhas.txt', 'r')


# Layout
sg.theme('Black')
layout = [
    [sg.Text('Usuário'),sg.Input(key='usuario', size=(20, 1))],
    # 'sg.Text' determina o texto que irá aparecer.
    # 'sg.Input' cria uma caixa de texto que recebe uma mensagem. 'Key' Recebe um identificador que pode ser usado mais abaixo.
    # 'Size' é o tamanho, 20 ´a largura e 1 a altura.
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*', size=(20, 1))],
    [sg.Checkbox('Salvar o login?', key='login')],
    [sg.Button('Entrar')]

]

# https://docs.pysimplegui.com/en/latest/documentation/module/themes/

# Janela
janela = sg.Window('Tela de Login', layout)
# Ler oe eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WIN_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] in loginsdad.read() and valores['senha'] in senhasdad.read():
            print(f'Bem vindo(a) {valores['usuario']}!')
    if valores['login']:
        if valores['usuario'] not in loginsdad.readline() or valores['senha'] not in senhasdad.readline():
            with open('logins.txt', 'a') as loginsDados:
                loginsDados.write(valores['usuario'] + '\n')
                loginsdad.close()
            with open('Senhas.txt', 'a') as senhaDados:
                senhaDados.write(valores['senha'] + '\n')
                senhasdad.close()
        else:
            break

