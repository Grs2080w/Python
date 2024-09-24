import urllib.parse
import urllib.request

s = urllib.request.urlopen('https://www.youtube.com/')
print(s)
# Abre um site, se não houver erro nenhum, não retorna erro

d = urllib.parse.urlparse('https://www.youtube.com/')
print(d)
# Mostra dados da Url.
