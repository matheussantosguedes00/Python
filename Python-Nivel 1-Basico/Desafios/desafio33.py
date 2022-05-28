
a=int(input('Valor 1° :'))
b=int(input('Valor 2° :'))
c=int(input('Valor 3° :'))

menor = a
if b<a and b<c:
     menor=b
if c<a and c<b:
    menor=c

maior = a
if b>a and b>c:
     maior=b
if c>a and c>b:
    maior=c

print('O menor valor e {}'.format(menor))
print('O maior valor e {}'.format(maior))