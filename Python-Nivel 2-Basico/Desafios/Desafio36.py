valorDaCasa = float(input('Valor da casa :R$'))
ValorDoSalario =float(input('Valor do salário :R$'))
quantAnos=int(input('Em quantos anos você vai pagar? :'))
minimo=ValorDoSalario*30/100

valorPac=valorDaCasa/(quantAnos*12)
print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de {:.2f}'.format(valorDaCasa,quantAnos,valorPac))

if valorPac<=minimo:
    print('Empréstimo aprovado')
else:
      print('Empréstimo negado')


