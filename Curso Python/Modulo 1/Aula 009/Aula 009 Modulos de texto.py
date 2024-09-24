frase = 'Ola mundo, tudo bem com você, como ta indo?'

print(frase[:5])#Mostra tudo desde o primeiro carácter ate o carácter do numero anterior mostrado no comando
print(frase[5:])#Mostra tudo a partir do carácter especificado até o final
print(frase[4:29])#Mostra tudo entre as posições dos carácteres informados no comando
print(frase[4:30:2])#O primeiro slot indica onde começa, o segundo onde acaba e o terceiro indica de quantas em quantas palavras ele vai pular.
#Colocando 0 nas duas primeiras posições, ele pode começar do início ou ir até o fim, 0 na última posição indica que ele não vai pular nenhuma letra.



len(frase)  #Mostra quantos carácteres tem na cadeia de palavras

frase.count('o', 0, 43)  #Mostra quanto da letra no comando tem no intervalo de carácteres

frase.find('ndo')  #Mostra em que número de carácter da frase a palavra pesquisada está
frase.find('android')  #Se a palavra digitada n tiver, ele mostra o numero -1

print('mundo' in frase)  #Mostra se tem a palavra desejada na frase com true ou false

frase.replace('mundo', 'planeta')  #Troca uma palavra pela outra na frase

frase.upper()  #Coloca todas as palavras/letras da frase em maiúsculo
frase.lower()  #Coloca todas as palavras/letras da frase em minúsculo

frase.capitalize()  #Coloca a primeira letra da frase em maiúsculo e o resto em minúsculo
frase.title()  #Coloca a primeira letra de cada palavra na frase em maiúsculo

frase.strip()#Remove todos os espaços inúteis no início e fim da frase
frase.rstrip()#Remove todos os espaços no lado direito da frase
frase.lstrip()#Remove todos os espaços do lado esquerdo da frase

frase.split()#Separa cada palavra da frase usando como padrão para separar, o espaço, e transforma em uma nova cadeia de palavras, onde cada palavra começa no carácter 0.
'-'.join(frase)#Junta as palavras peradas pelo split, e coloca entre as palavras o que tiver entre as aspas no inicio do comando
