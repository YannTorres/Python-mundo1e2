from random import randint
a = (randint(0, 2))
print('-=' * 6)
b = int(input('''SUAS OPÇÕES
[0] PEDRA
[1] PAPEL
[2] TESOURA
Qual sua opção: '''))
print('-=' * 6)
if a == 0:
    print('O Computador jogou PEDRA')
    if b == 0:
        print('Você jogou PEDRA\nJogo EMPATOU')
    elif b == 1:
        print('Você jogou PAPEL\nJogador GANHOU')
    elif b == 2:
        print('Você jogou TESOURA\nJogador PERDEU')
    else:
        print('Você jogou NADA porque é burro!')
elif a == 1:
    print('O Computador jogou PAPEL')
    if b == 0:
        print('Você jogou PEDRA\nJogador PERDEU')
    elif b == 1:
        print('Você jogou PAPEL\nJogo EMPATOU')
    elif b == 2:
        print('Você jogou TESOURA\nJogador GANHOU')
    else:
        print('Você jogou NADA porque é burro!')
elif a == 2:
    print('O Computador jogou TESOURA')
    if b == 0:
        print('Você jogou PEDRA\nJogador GANHOU')
    elif b == 1:
        print('Você jogou PAPEL\nJogador PERDEU')
    elif b == 2:
        print('Você jogou TESOURA\nJogo EMPATOU')
    else:
        print('Você jogou NADA porque é burro!')
