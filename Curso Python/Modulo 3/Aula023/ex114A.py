import urllib.request

try:
    urllib.request.urlopen('https://www.youtube.com')
except Exception as erro:
    print(erro.__class__)
else:
    print('To aqui!')


