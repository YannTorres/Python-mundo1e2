print('=' * 20)
print('{:^20}'.format('Banco Torres'))
print('=' * 20)
valor = int(input('Qual valor você deseja sacar? R$'))
total = valor
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total = total - céd
        totcéd = totcéd + 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao Banco Torres!')