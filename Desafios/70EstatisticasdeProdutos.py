print('-' * 20)
print('Mercado Torres')
print('-' * 20)
total = menor = cont = maiormil = 0
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$ '))
    cont = cont + 1
    total = total + preco
    if preco > 1000:
        maiormil = maiormil + 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break
print(f'O preço total dos produtos foi R${total:.2f}')
print(f'Tem {maiormil} produtos custando mais que R$1000')
print(f'O Produto mais barato é {barato} que custa R${menor:.2f}')
