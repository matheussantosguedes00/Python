n1 = int(input('Digite o primeiro numero :'))
n2 = int(input('Digite o segundo numero :'))
opicao = 0
while opicao != 5:
  print('[ 1 ] Somar')
  print('[ 2 ] Multiplicar')
  print('[ 3 ] Maior')
  print('[ 4 ] Novo números')
  print('[ 5 ] Sair do programa')
  opicao = int(input('>>>>>>Qual é sua opção ?'))
  if opicao == 1:
    print('Soma e iqual a {}.'.format(n1+n2))
  elif opicao == 2:
    print('Multipicação e iqual a {}.'.format(n1*n2))
  elif opicao==3:
      if n1>n2:
        print(' O maior é {}.'.format(n1))
      elif n2>n1:
        print(' O maior é {}.'.format(n2))
      else:
        print('São o mesmo números!')
  elif opicao==4:
     print('Informe os numeros novamente:')
     n1 = int(input('Digite o primeiro numero :'))
     n2 = int(input('Digite o segundo numero :'))
  elif opicao==5:
      print('FInalizando...')
  else:
    print('Opição inválida .Tente novamente')

print('=-='*10)
print('Fim do programa! Volte sempre!')

