from random import randint
print('=-' * 10)
print('Jogo Par ou Ímpar')
print('=-' * 10)
contador = 0
while True:
    n = int(input('Digite um valor: '))
    c = randint(0, 10)
    pi = str(input('Par ou Ímpar [P/I]: ')).strip().upper()[0]
    while pi not in 'PI':
        pi = str(input('Par ou Ímpar [P/I]: ')).upper()
    soma = n + c
    if soma % 2 == 0:
        print(f'Você jogou {n} e o computador jogou {c}, total de {soma} DEU PAR')
        if pi in 'P':
            print('Você ganhou')
            contador = contador + 1
        else:
            print('Você Perdeu')
            break
    elif soma % 2 == 1:
        print(f'Você jogou {n} e o computador jogou {c}, total de {soma} DEU ÍMPAR')
        if pi in 'I':
            print('Você Ganhou')
            contador = contador + 1
        else:
            print('Você perdeu')
            break
print(f'Você ganhou {contador} vezes')
