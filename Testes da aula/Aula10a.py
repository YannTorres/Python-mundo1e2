'''nome = str(input('Digite o seu nome: ')).strip().capitalize()
if nome != 'Yann':
    print('Nossa que nome feio!')
else:
    print('Nossa que nome lindo!')'''
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print(f'Sua média foi {m:.2f}')
if m >= 6.00:
    print('PARÁBENS')
else:
    print('ESTUDE MAIS')


