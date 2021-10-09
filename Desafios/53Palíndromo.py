f = str(input('Digite uma frase: ')).upper().strip().split()
f2 = ''.join(f)
g = f2[::-1]
print(f'O seu nome ao contrário fica: {g}')
if g == f2:
    print('Ele é um Palíndromo')
else:
    print('Ele não é um Palíndromo')
