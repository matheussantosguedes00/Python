veloci=float(input('Digite a velocidade de um carro :'))

if veloci>80:
    multa=(veloci-80)*7
    print('O carro ultrapassou o limite de velocidade')
    print('Sua multa e R${:.2f}'.format(multa))
else:
    print('Boa viagem!') 