anoDeNasc=int(input('Digite o ano de nascimento :'))

idade=2022-anoDeNasc
print('Idade :',idade)
if idade<=9:
    print('Mirim')
elif idade<=14:
    print('Infantil')
elif idade<=19:
    print('Junior')
elif idade<=20:
    print('Sênior')
else:
    print('Master')