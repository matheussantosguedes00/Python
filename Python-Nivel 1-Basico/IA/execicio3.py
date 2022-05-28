#3) Faça um programa que pergunte a distância que um passageiro deseja percorrer em Km. 
#Calcule o preço da passagem, cobrando R$ 0.50 por Km para viagens até 200Km e R$ 0.45 para 
#viagens mais longas.

distancia=float(input('Digite a distância que o passageiro deseja percorrer :'))

if(distancia<=200):
    dist1=distancia*0.50
    print('O valor da passagem é R$ {:.2f}.'.format(dist1))
else :
    dist2=distancia*0.45
    print('O valor da passagem é R$ {:.2f}.'.format(dist2))
 