from random import choice
a = input('Digite o nome do primeiro aluno: ')
b = input('Digite o nome do segundo aluno: ')
c = input('Digite o nome do terceiro aluno: ')
d = input('Digite o nome do quarto aluno: ')
nun_list = [a, b, c, d]

print(f'O aluno escolido foi: {choice(nun_list)}')
