anoDeNasc=int(input('Digite o ano de nascimento :'))

idade=2022-anoDeNasc


if idade<18:
    print('Anida vai se alistar')
    prazo=18-idade
    print('Falta {} ano para alistar'.format(prazo))
elif idade==18:
    print('Hora de se alistar ,sua idade e {} anos'.format(idade))
else:
    print('Passou do tempo do alistamento')
    prazo=idade-18
    print('Prazo do tempo {} ano para alistar'.format(prazo))

