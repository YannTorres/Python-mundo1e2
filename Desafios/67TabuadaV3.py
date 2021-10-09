while True:
    tabuada = int(input('Deseja ver qual tabuada? '))
    if tabuada < 0:
        break
    else:
        print('-' * 15)
        for c in range(1, 11):
            print(f'{tabuada} X {c} = {tabuada * c}')
        print('-' * 15)
print('Progama Encerrado, Volte sempre!!!')
