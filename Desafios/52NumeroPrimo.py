n = int(input('Digite um número: '))
div = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[31m', end=' ')
        div = div + 1
    else:
        print('\033[32m', end=' ')
    print(f'{c}', end=' ')
print(f'\n\033[mo numero {n} foi dividido {div} vezes')
if div > 2:
    print('Ele não é primo')
else:
    print('Ele é primo')
