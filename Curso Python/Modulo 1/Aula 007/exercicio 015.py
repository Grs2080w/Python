km = float(input('Quants kms foram percorridos?'))
dias = int(input('Por quantos dias o carro foi alugado?'))

cd = dias*605
ckm = km*0.15

ct = cd+ckm

print('O valor total a pagar é de R${}.'.format(ct))

#Legal