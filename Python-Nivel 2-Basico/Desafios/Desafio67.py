n=0
soma=0
while n>=-1:
    n=int(input('Digite um numero [número negativos parar a execução das tabuadas] :'))
    if n<0:
        print('Não e possivel usa numero negativos')
        break
    print('-'*30)
    print(f'TABUADA = {n}')
    for c in range(0,11):
        soma=n*c
        print(f'{n} X {c} = {soma}')
    
    