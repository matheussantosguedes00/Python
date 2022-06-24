num=0
cont=0
soma=0
while num != 999:
    soma=soma+num
    cont+=1
    num=int(input('Digite um número [999 para parar]: '))
print('Você digitou {} número e a soma entre eles e {}.'.format(cont-1,soma)) 
print('Acabou')