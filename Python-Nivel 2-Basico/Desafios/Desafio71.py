print('--'*15)
print('{:^30}'.format('Banco CEV'))
print('--'*15)

valor=int(input('Digite o valor que você quer sacar ? R$ '))
total=valor
ced = 50
totced=0
while True:
    if total>=ced:
       total=total-ced
       totced=totced+1
    else:
        if totced>0:
           print(f'Total de {totced} cédulas de R${ced}.')
        if ced==50:
           ced=20
           totced=0
        elif ced==20:
             ced=10
             totced=0
        elif ced==10:
             ced=1
             totced=0
        if total==0:
            break
