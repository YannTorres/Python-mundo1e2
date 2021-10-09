'''for c in range(1, 11):
    print(c)
print('Fim')'''
'''c = 1
while c < 10:
    print(c)
    c = c + 1
print('Fim')'''

'''for c in range(1, 3):
    n = int(input('Digite um valor: '))
print('Fim')'''
'''n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('Fim')'''
'''r = 's'
while r == 's':
    n = int(input('Digite um valor: '))
    r = str(input('Deseja continuar [S/N]: ')).lower()
print('Fim')'''
n = 1
par = impar = 0
while n != -1:
    n = int(input('Digite um número (digite -1 para parar): '))
    if n != -1:
        if n % 2 == 0:
            par = par + 1
        elif n % 2 == 1:
            impar = impar + 1
print(f'Você digitou {par} números pares e {impar} números ímpares')