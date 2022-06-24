r1=float(input('Digite comprimento da  1° reta :'))
r2=float(input('Digite comprimento da  2° reta :'))
r3=float(input('Digite comprimento da  3° reta :'))


if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Formar um triângulo')
    if r1==r2 ==r3:
        print('Equilátero')
    elif r1==r2 or r2==r3 or r1==r3:
        print('Isósceles')
    else:
        print('Escaleno')
else:
    print('Não formar um triangulo')