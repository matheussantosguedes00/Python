
print("=============Desafio 15============")

dias = int(input('Quantos dias alugados ?'))
km =float(input('Quantos km rodados?'))
pago=(dias*60) + (km*0.15)

print('Total a paga é de R${:.2f}' .format(pago))