print('-' * 28)
print('Analisador de Triângulos')
print('-' * 28)
s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))
if (s2 - s3) < s1 < s2 + s3 and (s1 - s3) < s2 < s1 + s3 and (s2 - s1) < s3 < s1 + s2:
    print('Com estes valores poderá se formar um triângulo')
else:
    print('Com estes valores NÃO poderá se formar um triângulo')
