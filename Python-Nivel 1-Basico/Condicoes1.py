nome=str(input('Qual e seu nome ?  '))
if nome=='Matheus':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tâo normal!')

print('Bom dia {}.'.format(nome))# sempre vai acontecer porque não esta esta colando no começor

print('-------------------------------------------------------')

n1=float(input('Digite a primeira nota :'))
n2=float(input('Digite a segunda nota :'))
media=(n1+n2)/2
print('A sua média foi {:.1f}'.format(media))

if media>=6.0:
    print('Sua média foi boa! PARABÈNS')
else:
    print('Sua média  foi ruim! ESTUDE MAIS! ')
    
print('-------------------------------------------------------')

n1=float(input('Digite a primeira nota :'))
n2=float(input('Digite a segunda nota :'))
media=(n1+n2)/2
print('A sua média foi {:.1f}'.format(media))

print('Sua média foi boa! PARABÈNS' if media>=6.0 else 'Sua média  foi ruim! ESTUDE MAIS! ' )


