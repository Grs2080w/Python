import random

suffixLength = 10

caracteres = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'

senha = ''
c = 0

while c <= suffixLength:
    indice = random.randint(0, len(caracteres) - 1 )
    senha += caracteres[indice]
    c += 1

print(senha)


generatedSuffix = senha

originalAddress = MailAddress("gabriel.2008grs@gmail.com")
generatedAddress = MailAddress(
    f"{originalAddress.user}+{generatedSuffix}@{originalAddress.host}")
print(generatedAddress)

# problema de instalação do Aspose