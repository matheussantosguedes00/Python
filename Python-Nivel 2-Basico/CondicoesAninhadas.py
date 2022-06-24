nome = input('Qual é seu nome? ')
if nome == 'Zoi':
    print('Que nome bonito!')
elif nome == 'João' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome e popular no Brasil.')
elif nome in 'Ana Claudia Jessica Juliana':
    print('Belo nome feminino')
else:
    print('Seu nome e bem normal.')
print('Tenha um bom dia, {}!'.format(nome))
