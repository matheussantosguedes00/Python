print("=============Desafio 20============")
import random
aluno1=input('Nome do aluno 1 :')
aluno2=input('Nome do aluno 2 :')
aluno3=input('Nome do aluno 3 :')
aluno4=input('Nome do aluno 4 :')

alunos=[aluno1,aluno2,aluno3,aluno4]
random.shuffle(alunos)
print('A ordem de apresentação sera ')
print(alunos)
print("=============Desafio  random mais from============")
from random import shuffle
aluno1=input('Nome do aluno 1 :')
aluno2=input('Nome do aluno 2 :')
aluno3=input('Nome do aluno 3 :')
aluno4=input('Nome do aluno 4 :')

alunos=[aluno1,aluno2,aluno3,aluno4]
shuffle(alunos)
print('A ordem de apresentação sera ')
print(alunos)