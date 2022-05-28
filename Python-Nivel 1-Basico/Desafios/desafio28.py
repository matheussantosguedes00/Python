from random import randint
from time import sleep
numero=randint(0,5)
print('-=-'*20)
print('\33[7;37m Vou pensar em um nùmero entre 0 e 5 .Tente adivinhar...\33[m')
print('-=-'*20)
print('\n')
usuario=int(input('Digite um numero:',))
print('\n')
print('\33[7;30;44m PROCESSANDO....\n\n\33[m')
sleep(3)

if usuario==numero:
    print('\33[1;37;40m==//==Parabens você acertou==//==\n')
    print('Numero do computador {} ,numero que você digitou {}\n\33[m'.format(numero,usuario))
    
else:
    print('\33[7;30;41m==//==Não e o nùmero certo==//==\n')
    print('Numero do computador {} ,numero que você digitou {}\n\33[m'.format(numero,usuario))
    
    
