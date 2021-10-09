from random import randint
from time import sleep

num = int(randint(0, 5))
print('-' * 40)
print('Estou pensando em um numero entre 0 e 5')
print('-' * 40)
num2 = int(input('Em que numero eu pensei: '))
print('')
print('Processando...')
sleep(1)
print('')
if num == num2:
    print('Parabéns você acertou')
else:
    print(f'Errado eu pensei no numero {num}')
