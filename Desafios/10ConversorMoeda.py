a = float(input('Há quantos reais em sua carteira? R$'))

print(f'Com R${a:.2f} você pode comprar US${a/5.47:.2f}')
print(f'Com R${a:.2f} você pode comprar EU€{a/6.62:.2f}')
