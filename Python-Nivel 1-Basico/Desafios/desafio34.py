sala=float(input('Digite seu salario ? R$ '))

if sala>=1250:
    aumento=(sala*10)/100
    novoSala=sala+aumento
    print('Seu novo salario e R${:.2f}.'.format(novoSala))
else:
     aumento=(sala*15)/100
     novoSala=sala+aumento
     print('Seu novo salario e RS{:.2f}.'.format(novoSala))
    