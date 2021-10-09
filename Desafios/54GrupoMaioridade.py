from datetime import date
cont = 0
cont2 = 0
for c in range(1, 8):
    a = int(input(f'Em que ano nasceu a {c}a pessoa: '))
    idade = date.today().year - a
    if idade >= 18:
        cont = cont + 1
    else:
        cont2 = cont2 + 1
print(f'Existem {cont} pessoas maiores de idade e {cont2} pessoas menores de idade ')