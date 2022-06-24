nota1=float(input('Nota 1 :'))
nota2=float(input('Nota 2 :'))
media=nota1+nota2
media2=media/2

print(media2)
if media2<5.0:
    print('Reprovado')
elif media2>=5.0 and media2<=6.9:
    print('Recuperação')
else:
    print('Aprovado')