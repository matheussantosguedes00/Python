media=0
con=0
con2=0
maisVelho=0
nomee=''
for c in range(1,5):
    print('--------------------------------------------------------')
    print('-----{}ª Pessoa-----'.format(c))
    nome = str(input('Digite seu nome :')).strip()
    idade=int(input('Digite seu idade :'))
    sexo =    input('Digite seu sexo [M/F] :').upper()
    media=media+idade
    if sexo=='F' and idade<20:
      con=con+1
    if sexo=='M'and idade>maisVelho:
      maisVelho=idade
      nomee=nome
print('--------------------------------------------------------')
print('O homem mais velho e {} e tem {} anos .'.format(nomee,maisVelho))
print('A Media de idade é {}'.format(media/4))
print('Mulheres com menos de 20 anos e apenas {}'.format(con))