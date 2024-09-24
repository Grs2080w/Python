velo = int(input('Qual sua velocidade?'))
if velo >= 80:
    print('Voce foi multado!')
    print('----Deverá pagar uma multa de R${}.----'.format((velo - 80) * 7))
else:
    print('\\\\\\Parabéns! Você está dento do limite de velocidade!////')