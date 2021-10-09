from datetime import date
ano = int(input('Digite um ano para calcular se este é bissexto, se quiser calcular o ano atual coloque 0: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'{ano} é um ano Bissexto')
else:
    print(f'{ano} não é um ano Bissexto')
