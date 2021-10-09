velocidade = float(input('Qual a velocidade atual do carro: '))
multa = (velocidade - 80) * 7
print('')
if velocidade <= 80:
    print('Você está dentro do limite')
else:
    print('Você foi multado por exeder o limite de velocidade de 80 km/h')
    print(f'O Valor da multa é R$ {multa:.2f}')

print('Bom dia, dirija com cuidado!')
