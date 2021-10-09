from time import sleep
n1 = int(input('Qual o primeiro valor: '))
n2 = int(input('Qual o segundo valor: '))
escolha = 0
while escolha != 5:
    print('''[1] Somar
[2] Multiplicar
[3] Maior número
[4] Novos números
[5] Sair do programa''')
    escolha = int(input('Digite a opção: '))
    if escolha == 1:
        n3 = n1 + n2
        print('-=' * 6)
        print(f'{n1} + {n2} = {n3} ')
        print('-=' * 6)
    elif escolha == 2:
        n3 = n1 * n2
        print('-=' * 6)
        print(f'{n1} * {n2} = {n3}')
        print('-=' * 6)
    elif escolha == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('-=' * 10)
        print(f'O maior número é {maior}')
        print('-=' * 10)
    elif escolha == 4:
        print('-=' * 16)
        n1 = int(input('Digite o primeiro novo valor: '))
        n2 = int(input('Digite o segundo novo valor: '))
        print('-=' * 16)
    elif escolha == 5:
        print('-=' * 10)
        print('Saindo...')
        print('-=' * 10)
    else:
        print('-=' * 17)
        print('Escolha inválida, tente novamente')
        print('-=' * 17)
    sleep(1.5)
    print('Programa finalizado')
