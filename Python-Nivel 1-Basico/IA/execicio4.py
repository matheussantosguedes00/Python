#4) Desenvolva um programa que leia o nome de um funcionário, seu salário, quantos anos ele 
#trabalha na empresa e mostre seu novo salário, reajustado de acordo com a tabela a seguir:
#- Até 3 anos de empresa: aumento de 3%
#-Entre 3 e 10 anos: aumento de 12.5%
#- 10 anos ou mais: aumento de 20%
nome=input('Digite seu nome :')
salario=float(input('Digite seu salario :'))
qtsAnos=float(input('Digite a quantidade de anos que trabalha na empresa :'))

if(qtsAnos<=3):
    reajuste=(salario*3)/100
    novoSalario=salario+reajuste
    print('Nome é {}, seu reajuste é  R${:.2f},Seu novo salario é R${:.2f}.' .format(nome,reajuste,novoSalario))
elif(qtsAnos>3 and qtsAnos<10):
     reajuste=(salario*12.5)/100
     novoSalario =salario+reajuste
     print('Nome é {}, seu reajuste é  R${:.2f},Seu novo salario é R${:.2f}.' .format(nome,reajuste,novoSalario))
else:
     reajuste=(salario*20)/100
     novoSalario =salario+reajuste
     print('Nome é {}, seu reajuste é  R${:.2f},Seu novo salario é R${:.2f}.' .format(nome,reajuste,novoSalario))
