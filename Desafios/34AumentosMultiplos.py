salario = float(input('Digite o Valor do seu salário: R$'))
if salario > 1250.00:
    novo = (salario * 10/100) + salario
    aumento = 10
else:
    novo = (salario * 15/100) + salario
    aumento = 15
print(f'Seu novo salário com aumento de {aumento}% será de R${novo} ')