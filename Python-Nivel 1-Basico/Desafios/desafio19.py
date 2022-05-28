print("=============Desafio 19============")
import random
aluno1=input('Nome do aluno 1 :')
aluno2=input('Nome do aluno 2 :')
aluno3=input('Nome do aluno 3 :')
aluno4=input('Nome do aluno 4 :')

alunos=[aluno1,aluno2,aluno3,aluno4]
escolhido=random.choice(alunos)
print('Nome escolhido foi : {} '.format(escolhido))

print("=============Desafio 19 randow com from============")
from random import choice
aluno1=input('Nome do aluno 1 :')
aluno2=input('Nome do aluno 2 :')
aluno3=input('Nome do aluno 3 :')
aluno4=input('Nome do aluno 4 :')

alunos=[aluno1,aluno2,aluno3,aluno4]
escolhido=choice(alunos)
print('Nome escolhido foi : {} '.format(escolhido))