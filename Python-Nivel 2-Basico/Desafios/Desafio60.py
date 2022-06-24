from math import factorial
n1=int(input('Digite um numero para calcular seu Fatorial :'))
f=factorial(n1)
print('O fatorial de {} é {}. '.format(n1,f))
print('------------------------------------------------------')

n11=int(input('Digite um numero para calcular seu Fatorial :'))
c=n11
fl=1
print('Calculando {}! = '.format(n11),end='')
while c>0:
    print(' {} '.format(c),end='')
    print('x' if c > 1 else ' = ',end='')
    fl=fl*c 
    c-=1
print(' {}'.format(fl))



