numeros = (int(input('Primeiro numero: ')), int(input('Segundo numero: ')),
           int(input('Terceiro numero: ')), int(input('Quarto numero: ')))
print(f'Você digitou os números {numeros}')
print(f'O valor 9 aparece {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O valor 3 aparece na {numeros.index(3) + 1}ª posição ')
else:
    print('O valor 3 não foi digitado')
cont = 0
for c in numeros:
    if c % 2 == 0:
        cont += 1
print(f'Foram digitados {cont} números pares ')
