maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input(f'Digite o peso da {c}a pessoa: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print(f'O maior peso foi {maior} e o menor peso foi {menor}')
