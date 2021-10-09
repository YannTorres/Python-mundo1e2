from random import randint
n = randint(0, 10)
print('Pensei em um número de 0 a 10')
p = 11
tentativa = 1
while p != n:
    p = int(input('Qual número eu pensei: '))
    if p == n:
        print('Parabéns você acertou!')
    elif p != n:
        if p < n:
            print('Você errou tente novamente! (shiiii.... foi um número maior)')
        elif p > n:
            print('Você errou tente novamente! (shiiii.... foi um número menor)')
        tentativa = tentativa + 1
print(f'Você precisou de {tentativa} tentativa(s) para acertar!')
