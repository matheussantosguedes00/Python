nome=input('Digite seu nome complento :')
nome.strip()
print('Nome Maiúsculo :{}'.format(nome.upper()))
print('Nome Minúsulos :',nome.lower())
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))

print ('Seu primeiro nome tem {} letras'.format(nome.find(' ')))#pode fazer desse jeito ou usa esse 

separa=nome.strip()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0],len(separa[0])))

