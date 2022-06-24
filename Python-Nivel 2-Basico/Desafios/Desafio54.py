

maiorI=0
menorI=0
for c in range(0,6):
    nasc=int(input('Digite o ano de nascimento :'))
   
    if 2022-nasc>=18:
     maiorI=maiorI+1
    else:
     menorI=menorI+1
print('Pessoas que são de maior de idade {}.\nPessoas que são de menor de idade {}'.format(maiorI,menorI))

#Ou pode fazer desse jeito 
#so colocar a data atual  e não precisa fica atualizando
from datetime import date
maiorI=0
menorI=0
atual=date.today().year
for c in range(0,6):
    nasc=int(input('Digite o ano de nascimento :'))
   
    if atual-nasc>=18:
     maiorI=maiorI+1
    else:
     menorI=menorI+1
print('Pessoas que são de maior de idade {}.\nPessoas que são de menor de idade {}'.format(maiorI,menorI))