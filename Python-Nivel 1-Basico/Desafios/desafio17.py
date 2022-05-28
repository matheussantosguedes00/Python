import math
from math import hypot

print("=============Desafio 17============")
cateoposto=float(input('Digite o cateto opostro :'))
cateoadjacente=float(input('Digite o cateto adjacente :'))
hipotenusa=(cateoposto**2 +cateoadjacente**2)**(1/2)
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))

print("=============Desafio 17 com math============")
cateoposto1=float(input('Digite o cateto opostro :'))
cateoadjacente1=float(input('Digite o cateto adjacente :'))
hipotenusa1=math.hypot(cateoposto1, cateoadjacente1)
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa1))

print("=============Desafio 17 com math e from============")
cateoposto1=float(input('Digite o cateto opostro :'))
cateoadjacente1=float(input('Digite o cateto adjacente :'))
hipotenusa1=hypot(cateoposto1, cateoadjacente1)
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa1))
