casa = float(input('Qual o valor do imóvel: R$'))
salario = float(input('Qual o salário do comprador: R$'))
anos = float(input('Em quantos anos o comprador vai financiar: '))

a = anos * 12
b = (casa/a)
c = salario * (30/100)
print('')
print(f'Para se pagar uma casa de {casa} em {anos:.0f} anos, será necessario uma prestação de R${b:.2f}')
if c > b:
    print('O valor está abaixo de 30 % do salário do comprador, EMPRÉSTIMO ACEITO')
else:
    print('O valor está acima de 30% do salário do comprador, EMPRÉSTIMO RECUSADO')
