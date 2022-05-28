distancia=float(input('Digite a distância que o passageiro deseja percorrer :'))

if(distancia<=200):
    dist1=distancia*0.50
    print('O valor da passagem é R$ {:.2f}.'.format(dist1))
else :
    dist2=distancia*0.45
    print('O valor da passagem é R$ {:.2f}.'.format(dist2))
 