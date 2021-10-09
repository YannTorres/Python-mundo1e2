continuar = 'S'
cont = media = soma = maior = menor = 0
while continuar in 'Ss':
    num = int(input('Digite um número: '))
    continuar = str(input('Deseja continuar [S/N]: '))
    cont += 1
    soma += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
print(f'A média dos {cont} números é de {soma/cont:.1f}')
print(f'O Maior número digitado foi {maior} e o menor foi {menor}')
