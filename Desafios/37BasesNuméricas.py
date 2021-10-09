num = int(input('Digite um número inteiro positivo: '))
base = int(input('''Escolha uma base para conversão:
[ 1 ] = Converter para binário
[ 2 ] = Converter para octal  
[ 3 ] = converter para hexadecimal
Sua opção: '''))

if base == 1:
    print(f'O número {num} convertido para binário é {bin(num)[2:]}')
elif base == 2:
    print(f'O número {num} convertido para octal é {oct(num)[2:]}')
elif base == 3:
    print(f'O número {num} convertido para hexadecimal é {hex(num)[2:]}')
else:
    print('Você tem problemas mentais???')
