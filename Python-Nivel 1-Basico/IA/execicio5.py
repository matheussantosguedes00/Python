#5) O Índice de Massa Corpórea (IMC) é um valor calculado baseado na altura e no peso de uma 
#pessoa. De acordo com o valor do IMC, podemos classificar o indivíduo dentro de certas faixas. 
#- Abaixo de 18.5: Abaixo do peso
#- Entre 18.5 e 25: Peso ideal
#- Entre 25 e 30: Sobrepeso
#- Entre 30 e 40: Obesidade
#- Acima de 40: Obesidade mórbida

nome=input('Digite seu nome :')
peso=float(input('Digite seu peso :'))
altura=float(input('Digite sua altura :'))

imc=peso/altura**2


if(imc<18.5) :
    print('IMC :',imc)
    print('Abaixo do peso')
elif(imc>=18.5 and imc<=25):
     print('IMC :{:.1f}'.format(imc))
     print('Peso ideal')
elif(imc>25 and imc<=30):
    print('IMC :{:.1f}'.format(imc))
    print('Sobrepeso')
elif(imc>30 and imc <=40):
    print('IMC :{:.1f}'.format(imc))
    print('Obesidade')
else:
    print('IMC :{:.1f}'.format(imc))
    print('Obesidade mórbida')





