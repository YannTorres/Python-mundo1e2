num = int(input('Deseja mostrar quantos termos da sequência de Fibonacci: '))
cont = 1
pt = 0
st = 1
soma = 1
print(f'0', end=' -> ')
while cont <= num:
    print(f'{soma}', end=' -> ')
    soma = pt + st
    cont = cont + 1
    pt = st
    st = soma
print('Fim')
