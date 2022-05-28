print("=============Desafio 18 math============")
import math
angulo=float(input('Digite o ângulo que você deseja: '))

seno=math.sin(math.radians(angulo))
print('O ângulo de {} tem o Seno  de {:.2f}'.format(angulo,seno))

cosseno=math.cos(math.radians(angulo))
print('O ângulo de {} tem o Cosseno  de {:.2f}'.format(angulo,cosseno))

tangente =math.tan(math.radians(angulo))
print('O ângulo de {} tem o Tangente  de {:.2f}'.format(angulo,tangente))


print("=============Desafio 18 math e from============")
from math import sin, cos, tan,radians
angulo=float(input('Digite o ângulo que você deseja: '))

seno=sin(radians(angulo))
print('O ângulo de {} tem o Seno  de {:.2f}'.format(angulo,seno))

cosseno=cos(radians(angulo))
print('O ângulo de {} tem o Cosseno  de {:.2f}'.format(angulo,cosseno))

tangente =tan(radians(angulo))
print('O ângulo de {} tem o Tangente  de {:.2f}'.format(angulo,tangente))
