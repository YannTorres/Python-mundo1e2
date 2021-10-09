from math import sqrt
cato = float(input('Digite o comprimento do cateto oposto: '))
cata = float(input('Digite o comprimento do cateto adjacente: '))

hip = sqrt((cata**2) + (cato**2))

print(f'A hipotenusa vale {hip:.2f}')
