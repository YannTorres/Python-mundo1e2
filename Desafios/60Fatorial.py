n = int(input('Digite um numero para saber seu fatorial: '))
c = n
f = 1
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f = f * c
    c -= 1
print(f)
'''n = int(input('Digite um numero para saber seu fatorial: '))
c = n
f = 1
for c in range(1, n):
    f = f * n
    n = n - 1
print(f'Seu fatorial é {f}')'''