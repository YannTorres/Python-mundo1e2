c1 = int(input('Por quantos dias foi rodado: '))
c2 = float(input('Quantos km foi rodado: '))

d1= c1*60
d2= c2*0.15

print(f'O Valor a ser pago pelo aluguel do carro é de R${d1+d2:.2f}')
