n=0
cont=0
soma=0
while n!=999:
    n=int(input('Digite um numero [999 para parar] :'))
    if n==999:
        break
    cont=cont+1
    soma=soma+n

print(f'Foi digitando {cont} números e sua soma e igual a {soma}.')
