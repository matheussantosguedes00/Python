"""cont=1
while True:
    print(cont,' -> ',end='')
    cont +=1
print('Acabou')"""

"""n=0
s=0
while n != 999:
    s=s+n
    n=int(input('Digite um número :')) //para a soma sem fazer gambiarra e sem usa o -999
print('A soma vale {}'.format(s))
""" 

n=0
s=0
while n != 999:
    n=int(input('Digite um número :'))
    if n==999:
        break
    s=s+n
print('A soma vale {}'.format(s))#pode usa desse dois jeito que vai chegar no mesmo resultado
print(f'A soma e {s}')

nome='Matheus'
idade=21

print(f'O {nome} tem {idade} anos.')# e usando no python 3.6+
print('O {} tem {} anos.'.format(nome, idade))# e usando no python 3.5+
print('O %s tem %d anos.'% (nome,idade))# usando no python artigo mais ainda funciona


nome1='Zoi'
idade1=20
salario=1212.3
print(f'O {nome} tem {idade} anos e ganha R$ {salario:.2f}.')
