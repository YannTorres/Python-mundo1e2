'''import random
frase = input('Escreva o nome dos três alunos entre espaços: ')
frase.split()

print(f'A ordem dos alunos será {random.sample(frase, k=3)}')'''

'''frase = 'Curso em Vídeo Python'
print('urso' in frase)'''

frase = 'Curso em Vídeo Python'
dividido = frase.split()
junto = '-'.join(dividido)

print(dividido)
print(junto)
