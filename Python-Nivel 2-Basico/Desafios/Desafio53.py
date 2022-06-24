frase=str(input('Digite uma frase :')).strip().upper()
palavras=frase.split()#divide a palavras
tudoJunto=''.join(palavras)# junta tudo sem espaço
inverso=''
for letra in range(len(tudoJunto)-1,-1,-1):#len pega a ultima letra 
     inverso +=tudoJunto[letra]
print('O inverso de {} é {}.'.format(tudoJunto,inverso))
if tudoJunto==inverso:
    print('A frase e uma Palíndromo.')
else:
    print('Não e uma Palíndromo')

#ou pode fazer dessa forma

frase=str(input('Digite uma frase :')).strip().upper()
palavras=frase.split()#divide a palavras
tudoJunto=''.join(palavras)# junta tudo sem espaço

inverso=tudoJunto[::-1]

print('O inverso de {} é {}.'.format(tudoJunto,inverso))
if tudoJunto==inverso:
    print('A frase e uma Palíndromo.')
else:
    print('Não e uma Palíndromo')

