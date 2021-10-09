totalmais18 = homens = mulheresmenos20 = 0
while True:
    print('-=' * 10)
    print('Cadastre uma Pessoa')
    print('-=' * 10)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    print('-=' * 10)
    if idade > 18:
            totalmais18 = totalmais18 + 1
    if sexo == 'M':
            homens = homens + 1
    if sexo == 'F' and idade < 20:
            mulheresmenos20 = mulheresmenos20 + 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        print('-=' * 10)
        print('Progama finalizado')
        break

print(f'Total de pessoas com mais de 18 anos: {totalmais18}')
print(f'Total de Homens cadastrados: {homens}')
print(f'Total de Mulheres com menos de 20 anos: {mulheresmenos20}')