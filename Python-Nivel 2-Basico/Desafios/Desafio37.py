nume = int(input('Digite um numero:'))

opicao = int(input('---Menu---\n[1]Converter para binário\n[2]Converter para octal\n[3]Converter para hexadecimal\n Sua opição é :'))

if opicao == 1:
    print('{} convertido para Binário é igual a {} '.format(nume,bin(nume)[2:]))
elif opicao == 2:
    print('{}convertido para Octal é igual a {} '.format(nume,oct(nume)[2:]))
elif opicao == 3:
    print('{}convertido para Hexadecimal é igual a {} '.format(nume,hex(nume)[2:]))
else:
    print('Essa opição não esta disponivel')
