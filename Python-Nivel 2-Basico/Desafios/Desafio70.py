print('--'*15)
print('Loja super Baratão')
print('--'*15)
compra=0
maisDemil=0
menorP=0
cont=0
barato=' '
while True:
    nome=str(input('Nome do Produto : '))
    preco=float(input('Preço do Produto : R$'))
    cont=cont+1
    compra=compra+preco
    if preco>1000:
       maisDemil=maisDemil+1
    if cont == 1 or preco < menorP:
       menorP = preco
       barato=nome
   
    escolha =' '
    while escolha not in 'SN':
       escolha=str(input('Quer continuar? [S/N] :')).strip().upper()[0]
    if escolha=='N':
         break

print(f'O total da compra foi R$ {compra:.2f}')
print(f'Temos {maisDemil} produto que esta custando mais de R$ 1000.')
print(f'O produto mais barato foi {barato} que custa R$ {menorP:.2f}')
