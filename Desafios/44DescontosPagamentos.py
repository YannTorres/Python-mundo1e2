print('\033[35m-=' * 8)
print('\033[34mMERCADINHO YANN\033[m')
print('\033[35m-=\033[m' * 8)
p = float(input('Qual o preço total das compras: R$'))
print('''FORMAS DE PAGAMENTO
[1] À vistá Dinheiro
[2] À vista Cartão
[3] 2x no Cartão
[4] 3x ou mais no Cartão''')
a = int(input('Qual opção: '))
if a == 1:
    print(f'O valor da sua compra passará de R${p:.2f} para R${p - (10/100) * p:.2f} com 10% de desconto')
elif a == 2:
    print(f'O valor da sua compra passará de R${p:.2f} para R${p - (5/100) * p:.2f} com 5% de desconto')
elif a == 3:
    print(f'O valor de suas compras será R${p:.2f} com 2x parcelas de R${p / 2:.2f}')
elif a == 4:
    b = int(input('Quantas parcelas serão:'))
    print(f'O valor de suas compras será R${p + (20/100) * p:.2f} por ter 20% de juros')
    print(f'Serão {b}x parcelas de R${(p + (20/100) * p) / b:.2f}')
else:
    print('\033[31mVocê tem problemas mentais!')
