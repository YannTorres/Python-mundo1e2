numero = int(input('Digite um número de 0 á 9999: '))
numero2= str(int(10000 + numero))

print(f'Unidades: {numero2[4]}')
print(f'Dezenas: {numero2[3]}')
print(f'Centenas: {numero2[2]}')
print(f'Milhares: {numero2[1]}')
