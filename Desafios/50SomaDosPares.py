soma = 0
cont = 0
for c in range(1, 7):
    a = int(input(f'Digite o {c} numero: '))
    if a % 2 == 0:
        soma = soma + a
        cont = cont + 1
print(f'A soma dos {cont} numeros pares informados é {soma}')


