numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
           'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze',
           'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    escolha = int(input('Digite um número entre 0 e 20: '))
    if 20 >= escolha >= 0:
        break
    print('Tente novamente...')
print(f'Você digitou o número {escolha} que em extenso é {numeros[escolha]}')

