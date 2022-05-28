#1) Escreva um programa que pergunte a velocidade de um carro. Caso ultrapasse 80Km/h, exiba 
#uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando 
#R$ 5,00 por cada Km acima da velocidade permitida

velocidade=float(input('Digite a velocidade do carro : '))

if(velocidade>80):
    print('====Usuário foi Multado===')
    valorDaMulta=(velocidade-80)*5
    print('O valor da multa e R$5,00 por cada Km acima da velocidade permitida')
    print('O valor da sua multa e R${:.2f} '.format(valorDaMulta))
else :
    print('Usuário não ultrapasso o limite de velocidade. ')