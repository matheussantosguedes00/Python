sexo=str(input('Digite o seu sexo : [M/F]')).strip().upper()[0]

while sexo not in 'MmFf':
    sexo=str(input('Dados iválidos. Por favor, Informe seu sexo :')).strip().upper()[0]

print ('Sexo {} registado com sucesso.'.format(sexo))


