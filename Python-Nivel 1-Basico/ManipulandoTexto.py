frase = 'Curso em Video Python'
print(frase)#frase completa 
print('--------------------------------------')
print(frase[4])#A letra numero 4 da frase 
print('--------------------------------------')
print(frase[3:13])#Da terceira posição ate a 13
print('--------------------------------------')
print(frase[:13])#Do inicio ate a posição 13
print('--------------------------------------')
print(frase[13:])# Do 13 ate o final
print('--------------------------------------')
print(frase[1:15:2])# Do uma ate a posição 15 pulando de dois em dois
print('--------------------------------------')
print(frase[::2])# Não saber o inicio e nem o final mais vai pulando de dois em dois 
print('--------------------------------------')
print("""pkoaweeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
eeeeeeeeeeeeeuriadohfbvvvvvvvvvvvvvvvvvvvvvv
vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvved
abhjhjhjhjhjhjhjhjhjhjhjhjhjhjhjh
jhjhjhjhjhjhjhjhjhjhjhjhjhjhjhjhjhjhjhjhjhjhjhjhjf""")#Pode""" usa para texto grande 
print('--------------------------------------')
print(frase.count('o'))#Quantidade de letras o na frase
print('--------------------------------------')
print(frase.upper().count('O'))#Vai colocar todas as letras maiusculo e depois vai ver quantidade de letras O na frase
print('--------------------------------------')
print(len(frase))# Vai ver a quantidades de letras e espaço na frase
print('--------------------------------------')
print(len(frase.split()))# Vai ver a quantidades de letras e espaço na frase e o split() vai tira o espaço no começo  e fim
print('--------------------------------------')
print(frase.replace('Python','Android'))#Troca a palavra python por android so aqui que mandar mais a frase continua a mesma
print('--------------------------------------')
frase=frase.replace('Python','Android')#Troca a palavra python por android 
print(frase)
print('--------------------------------------')
print('Curso'in frase) #Ver se tem  a palavra na frase e retorna true ou false
print('--------------------------------------')
print (frase.find('Curso'))#mostra a posição da palavra tem que se iqual senão vai retorna -1
print('--------------------------------------')
print(frase.lower())#frase esta minuscula
print('--------------------------------------')
print(frase.split())#Pode dividir palavras pode tambem escolhe a letra que vai aparecer
print('--------------------------------------')
