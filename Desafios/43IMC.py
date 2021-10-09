p = float(input('Qual o seu peso em Kilos: '))
a = float(input('Qual a sua altura em Metros: '))
imc = p / (a * a)
print(f'O seu IMC é {imc:.1f}:')
if imc < 18.5:
    print('CLASSIFICAÇÃO: ABAIXO DO PESO')
elif imc < 25:
    print('CLASSIFICAÇÃO: PESO IDEAL')
elif imc < 30:
    print('CLASSIFICAÇÃO: SOBREPESO')
elif imc < 40:
    print('CLASSIFICAÇÃO: OBESIDADE')
else:
    print('CLASSIFICAÇÃO: OBESIDADE MÓRBIDA')
