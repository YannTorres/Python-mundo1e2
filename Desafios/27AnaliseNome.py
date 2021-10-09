nome = str(input('Escreva o seu nome completo: ')).strip()
nome2 = nome.split()

print(f'Prazer em te conheçer {nome}')
print(f'Seu primeiro nome é {nome2[0]}')
print(f'Seu último nome é {nome2[len(nome2)-1]}')
