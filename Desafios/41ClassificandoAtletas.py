from datetime import date
a = int(input('Digite o ano de nascimento: '))
i = date.today().year - a
print(f'Quem nasceu em {a} tem {i} anos de idade')
if i <= 9:
    print('Classificação: MIRIM')
elif i <= 14:
    print('Classificação: INFANTIL')
elif i <= 19:
    print('Classificação: JUNIOR')
elif i <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')
