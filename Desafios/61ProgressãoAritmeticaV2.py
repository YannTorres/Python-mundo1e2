n1 = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a Razão: '))
termo = n1
cont = 1
while cont <= 10:
    print(f'{termo} -> ', end='')
    termo = termo + razao
    cont = cont + 1
print('Fim')
'''for c in range(n1, n1 + 10 * razao, razao):
    print(c, end=' -> ')
print('FIM')'''
