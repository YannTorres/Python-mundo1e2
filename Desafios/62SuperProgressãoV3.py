n1 = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a Razão: '))
termo = n1
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} -> ', end='')
        termo = termo + razao
        cont = cont + 1
    print('Pausa')
    mais = int(input('Quantos termos vc deseja mostrar a mais: '))
print(f'Foram exibidos {total} termos')