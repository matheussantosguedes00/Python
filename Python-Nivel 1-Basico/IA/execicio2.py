#2) Faça um programa que leia o ano de nascimento de uma pessoa, calcule a idade dela e depois 
#mostre se ela pode ou não votar.

anoDeNascimento=int(input('Digite seu ano de nascimento :'))

idade=2022-anoDeNascimento

if(idade>=16):
    print('Sua idade é {}'.format(idade))
    print('Pode votar')
else :
    print('Sua idade é {}'.format(idade))
    print('Não pode votar')
