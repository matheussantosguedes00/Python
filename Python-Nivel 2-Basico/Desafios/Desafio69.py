tp=0
ho=0
mu=0
Sexo= ' '
escolha= ' '
while True:
   print('--'*10)
   print('CADASTRE UMA PESSOA')
   print('--'*10)
   Idade=int(input('IDADE :'))
   while Sexo not in 'MF':
      Sexo=str(input('SEXO [M/F] :')).strip().upper()[0]
   if Idade >18:
     tp=tp+1
   if Sexo=='M':
     ho=ho+1
   if Sexo=='F'and Idade<20:
     mu=mu+1
   while escolha not in 'SN':
      escolha=str(input('Quer continuar? [S/N] :')).strip().upper()[0]
   if escolha=='N':
     break
print(f'Total de pessoas com mais de 18 anos e :{tp}')
print(f'Ao todo temos {ho} homens cadastrados')
print(f'E temos {mu} com menos de 20 anos')
