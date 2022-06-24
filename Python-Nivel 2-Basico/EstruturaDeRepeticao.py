for c in range(6, 0, -1):
    print(c)
print('fim')
for c in range(0, 7, 2):
    print(c)
print('fim')

numero=int(input('Digite um número :'))
for c in range(0,numero+1):
    print(c)
print('fim')

i=int(input('Inicio :'))
f=int(input('fim :'))
p=int(input('Passo :'))
for c in range(i ,f+1 ,p):
    print(c)
print('fim')

s=0
for c in range(0, 3):
    n= int(input('Digite um valor :'))
    s=s+n # ou s+=n
print('A soma dos valores digitados foi {}.'.format(s))