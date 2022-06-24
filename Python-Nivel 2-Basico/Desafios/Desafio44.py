produto=float(input('Valor do produto :'))
print('\n')
opicao=int(input('----Menu---- \n1:Dinheiro ou cheque.\n2:Cartão.\n3:Duas vezes no cartão.\n4:Três vezes no cartão\nOpição : '))

if opicao==1:
    print('Valor do produto : {:.2f}'.format(produto))
    desc=produto*10/100
    print('Novo valor apos o desconto e {:.2f}'.format(produto-desc))
elif opicao==2:
     print('Valor do produto : {:.2f}'.format(produto))
     desc=produto*5/100
     print('Novo valor apos o desconto e {:.2f}'.format(produto-desc))
elif opicao==3:
     print('Valor do produto : {:.2f}'.format(produto))
elif opicao==4:
     print('Valor do produto : {:.2f}'.format(produto))
     desc=produto*20/100
     print('Novo valor apos o desconto e {:.2f}'.format(desc+produto))
else:
    print('Essa opção não tem')

    