from random import randint
from time import sleep
itens=('Pedra','Papel','Tesoura')
pc=randint(0,2)
opicao=int(input('Suas opções :\n[0]PEDRA\n[1]PAPEL\n[2]TESOURA\nQual e sua Jogada ? '))
print('JO')
sleep(1)
print('KEM')
sleep(1)
print('PO!!!')
print('-='*14)
print('O computador jogou {}'.format(itens[pc]))
print('Jogador jogou {}'.format(itens[opicao]))
print('-='*14)

if pc==0:

   if opicao==0:
      print('Empate')
   elif opicao==1:
      print('JOGADOR VENCER')
   elif opicao==2:
      print('PC VENCER')
   else:
      print('JOGADA INVÀLIDA!')

elif pc==1:
   if opicao==0:
      print('PC VENCER')
   elif opicao==1:
      print('Empate')
   elif opicao==2:
       print('JOGADOR VENCER')
   else:
      print('JOGADA INVÀLIDA!')

elif pc==2:
   if opicao==0:
     print('JOGADOR VENCER')
   elif opicao==1:
       print('PC VENCER')
   elif opicao==2:
    print('Empate')

   else:
      print('JOGADA INVÀLIDA!')
